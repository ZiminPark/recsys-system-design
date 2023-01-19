import os
from dataclasses import dataclass
from typing import Any, Dict

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis

load_dotenv()


r = Redis(host=os.environ["REDIS_ADDRESS"], port=int(os.environ["REDIS_PORT"]))
app = FastAPI()


class RecommenderRequest(BaseModel):
    user_id: int


@dataclass
class User:
    _id: int
    age: int

    @property
    def category(self) -> str:
        if self.age < 10:
            return "kid"
        elif self.age < 20:
            return "teenage"
        else:
            return "adult"


@app.post("/recommend")
def recommend(req: RecommenderRequest) -> Dict[str, Any]:
    mp = {"kid": "Toy", "teenage": "Book", "adult": "Car"}
    age = r.get(f"sample:feature:userId:{req.user_id}:age").decode("utf-8")
    user = User(req.user_id, int(age))
    item = mp.get(user.category, "No Item is recommended.")

    return {"category": user.category, "item": item, "age": age}


@app.post("/click")
def click(req: RecommenderRequest) -> Dict[str, Any]:
    num_click = r.incr(f"event:userId:{req.user_id}:click")
    return {"num_click": num_click}


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("BACKEND_HOST", "localhost")
    port = int(os.getenv("BACKEND_PORT", 8000))
    uvicorn.run("main:app", host=host, port=port, reload=True)
