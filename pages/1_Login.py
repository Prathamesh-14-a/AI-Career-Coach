import streamlit as st

from src.auth.auth_service import login
from src.auth.session_manager import create_session, is_authenticated


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
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

st.title("🔐 Login")

st.write(
    "Welcome back to AI Career Coach"
)

email = st.text_input(
    "Email",
    placeholder="Enter your email"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)

login_btn = st.button(
    "Login",
    use_container_width=True
)

# --------------------------------------------------
# LOGIN LOGIC
# --------------------------------------------------

if login_btn:

    if not email or not password:
        st.warning(
            "Please fill all fields"
        )

    else:

        try:

            user = login(
                email=email,
                password=password
            )

            create_session(user)

            st.success(
                "Login Successful"
            )

            st.switch_page(
                "pages/3_Dashboard.py"
            )

        except Exception as e:

            st.error(
                str(e)
            )

# --------------------------------------------------
# SIGNUP LINK
# --------------------------------------------------

st.divider()

col1, col2 = st.columns([3, 2])

with col1:
    st.write("Don't have an account?")

with col2:
    if st.button("Sign Up"):
        st.switch_page(
            "pages/2_Signup.py"
        )