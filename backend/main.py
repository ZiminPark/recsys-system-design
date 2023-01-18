from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


class RecommenderRequest(BaseModel):
    user_id: int
    age: int


class User(BaseModel):
    age: int

    @property
    def category(self) -> str:
        if self.age < 5:
            return "kid"
        else:
            return "child"


app = FastAPI()


@app.post("/recommend")
def recommend(req: RecommenderRequest) -> Dict[str, str]:
    mp = {
        "kid": "Toy",
        "child": "Book",
    }
    user = User(age=req.age)
    item = mp.get(user.category, "No Item is recommended.")

    return {"category": user.category, "item": item}


if __name__ == "__main__":
    import os

    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()

    host = os.environ["BACKEND_HOST"]
    port = int(os.environ["BACKEND_PORT"])

    uvicorn.run("main:app", host=host, port=port, reload=True)
