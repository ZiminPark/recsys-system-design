import os
import random

from dotenv import load_dotenv
from redis import Redis


def init(host: str = "localhost", port: int = 6379, db: int = 0):
    return Redis(host, port, db)


def generate_sample_data(r: Redis, num_users: int = 100, age_range: tuple = (0, 30)):
    for i in range(num_users):
        r.set(f"sample:feature:userId:{i}:age", random.randint(*age_range))


if __name__ == "__main__":
    load_dotenv()
    r = init(os.environ["REDIS_ADDRESS"], int(os.environ["REDIS_PORT"]))
    generate_sample_data(r)
