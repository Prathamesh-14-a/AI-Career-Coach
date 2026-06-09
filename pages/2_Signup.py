import streamlit as st

from src.auth.auth_service import signup
from src.auth.session_manager import (
    create_session,
    is_authenticated
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Sign Up",
    page_icon="📝",
    layout="centered"
)

# --------------------------------------------------
# REDIRECT IF ALREADY LOGGED IN
# --------------------------------------------------

if is_authenticated():
    st.switch_page("pages/3_Dashboard.py")

# --------------------------------------------------
# UI
# --------------------------------------------------

st.title("📝 Create Account")

st.write(
    "Join AI Career Coach and start building your career."
)

username = st.text_input(
    "Username",
    placeholder="Enter your username"
)

email = st.text_input(
    "Email",
    placeholder="Enter your email"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Create a password"
)

confirm_password = st.text_input(
    "Confirm Password",
    type="password",
    placeholder="Confirm your password"
)

signup_btn = st.button(
    "Create Account",
    use_container_width=True
)

# --------------------------------------------------
# SIGNUP LOGIC
# --------------------------------------------------

if signup_btn:

    if (
        not username
        or not email
        or not password
        or not confirm_password
    ):
        st.warning(
            "Please fill all fields."
        )

    elif password != confirm_password:
        st.error(
            "Passwords do not match."
        )

    elif len(password) < 8:
        st.error(
            "Password must be at least 8 characters."
        )

    else:

        try:

            user = signup(
                username=username,
                email=email,
                password=password
            )

            create_session(user)

            st.success(
                "Account created successfully!"
            )

            st.switch_page(
                "pages/3_Dashboard.py"
            )

        except Exception as e:

            st.error(
                str(e)
            )

# --------------------------------------------------
# LOGIN LINK
# --------------------------------------------------

st.divider()

col1, col2 = st.columns([3, 2])

with col1:
    st.write(
        "Already have an account?"
    )

with col2:
    if st.button("Login"):
        st.switch_page(
            "pages/1_Login.py"
        )