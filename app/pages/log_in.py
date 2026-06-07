import streamlit as st

from src.auth.auth_service import login
from src.auth.session_manager import (
    create_session
)

st.title("Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    try:

        user = login(
            email=email,
            password=password
        )

        create_session(user)

        st.success(
            f"Welcome {user.username}"
        )

        st.switch_page(
            "pages/Dashboard.py"
        )

    except ValueError as e:
        st.error(str(e))

    except Exception as e:
        st.error(
            f"Unexpected error: {e}"
        )