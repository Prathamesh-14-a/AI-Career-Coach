import streamlit as st

st.set_page_config(
    page_title="DataPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 DataPilot AI")
st.caption("Navigate Your Data Career with AI")

st.subheader(
    "Your AI Copilot for Data Science & AI Careers"
)

st.write(
    """
    Welcome to DataPilot AI.

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