import requests  # type: ignore

import streamlit as st

user_id = st.number_input("User ID", min_value=0, max_value=100, value=10)
age = st.number_input("Age", min_value=0, max_value=100, value=10)
res = requests.api.post(
    "http://localhost:8000/recommend", json={"user_id": user_id, "age": age}
)

if st.checkbox("Show response"):
    st.json(res.json())
