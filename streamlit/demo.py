import os

import requests
from dotenv import load_dotenv

import streamlit as st


def get_url() -> str:
    BACKEND_HOST = os.environ["BACKEND_HOST"]
    PORT = os.environ["BACKEND_PORT"]

    backend_url = f"{BACKEND_HOST}:{PORT}"
    return backend_url


load_dotenv()
backend_url = get_url()


user_id = st.number_input("User ID", min_value=0, max_value=100, value=10)
age = st.number_input("Age", min_value=0, max_value=100, value=10)

if st.checkbox("Show response"):
    res = requests.api.post(
        f"{backend_url}/recommend", json={"user_id": user_id, "age": age}
    )
    st.json(res.json())
