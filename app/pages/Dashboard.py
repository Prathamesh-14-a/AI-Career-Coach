import streamlit as st

from src.auth.session_manager import (
    is_authenticated,
    logout
)

if not is_authenticated():
    st.error("Please login first")
    st.stop()

st.title("Dashboard")

st.write(
    f"Welcome {st.session_state['username']}"
)

st.write(
    f"Email: {st.session_state['email']}"
)

if st.button("Logout"):
    logout()
    st.switch_page(
        "pages/Login.py"
    )