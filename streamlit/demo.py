import os
from logging import getLogger

import requests
from dotenv import load_dotenv
from redis import Redis

import streamlit as st

logger = getLogger(__name__)


def get_url() -> str:
    BACKEND_HOST = os.environ["BACKEND_HOST"]
    PORT = os.environ["BACKEND_PORT"]

    backend_url = f"{BACKEND_HOST}:{PORT}"
    return backend_url


def post_click_event(user_id: int, item: str):
    body = requests.api.post(
        f"http://{backend_url}/click", json={"user_id": user_id, "item_id": item}
    ).json()
    logger.info(f"Click cnt: {body['num_click']}")
    return body["num_click"]


load_dotenv()
backend_url = get_url()
r = Redis(host=os.environ["REDIS_ADDRESS"], port=int(os.environ["REDIS_PORT"]))


user_id = st.number_input("userId", min_value=0, max_value=100, step=1)


if st.checkbox("Show response for selected user"):
    res = requests.api.post(
        f"http://{backend_url}/recommend", json={"user_id": user_id}
    )
    st.text(f"User ID: {user_id}")

    body = res.json()
    st.json(body)

    if st.button("Like?"):
        num_click = post_click_event(int(user_id), body["item"])
        st.text(f"user {user_id} click {body['item']} {num_click} times")
