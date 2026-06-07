import streamlit as st

from src.auth.auth_service import signup


st.title("Create Account")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input(
    "Password",
    type="password"
)

confirm_password = st.text_input(
    "Confirm Password",
    type="password"
)

if st.button("Signup"):

    if not username:
        st.error("Username is required")

    elif not email:
        st.error("Email is required")

    elif password != confirm_password:
        st.error("Passwords do not match")

    else:
        try:

            user = signup(
                username=username,
                email=email,
                password=password
            )

            st.success(
                f"Account created for {user.username}"
            )

        except ValueError as e:
            st.error(str(e))

        except Exception as e:
            st.error(
                f"Unexpected error: {e}"
            )