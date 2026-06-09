import streamlit as st

st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Coach")

st.write(
    """
    Welcome to AI Career Coach.

    Features:
    - Resume Analyzer
    - Skill Analysis
    - Salary Predictor
    - AI Career Mentor
    - Market Insights
    """
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Login", use_container_width=True):
        st.switch_page("pages/1_Login.py")

with col2:
    if st.button("Sign Up", use_container_width=True):
        st.switch_page("pages/2_Signup.py")