import os

import requests
from dotenv import load_dotenv
from redis import Redis

import streamlit as st


def get_url() -> str:
    BACKEND_HOST = os.environ["BACKEND_HOST"]
    PORT = os.environ["BACKEND_PORT"]

    backend_url = f"{BACKEND_HOST}:{PORT}"
    return backend_url


load_dotenv()
backend_url = get_url()
r = Redis(host=os.environ["REDIS_ADDRESS"], port=int(os.environ["REDIS_PORT"]))


user_id = st.number_input("userId", min_value=0, max_value=100, step=1)


if st.checkbox("Show response for selected user"):
    res = requests.api.post(
        f"http://{backend_url}/recommend", json={"user_id": user_id}
    )
    st.text(f"User ID: {user_id}")
    st.json(res.json())
