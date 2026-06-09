import streamlit as st

from src.auth.session_manager import (
    is_authenticated,
    logout
)

if not is_authenticated():
    st.warning("Please login first")
    st.stop()
from components.sidebar import show_sidebar

show_sidebar()
# Header
st.title("🏠 Dashboard")

st.write(
    f"Welcome back, {st.session_state['username']} 👋"
)

st.caption(
    "Your AI Copilot for Data Careers"
)

# Metric Section
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "ATS Score",
        "82%"
    )

with col2:
    st.metric(
        "Skill Match",
        "74%"
    )

with col3:
    st.metric(
        "Expected Salary",
        "₹8.5 LPA"
    )

# Quick Actions
st.subheader("🚀 Quick Actions")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "📄 Resume Analyzer",
        use_container_width=True
    ):
        st.switch_page(
            "pages/4_Resume_Analyzer.py"
        )

    if st.button(
        "💰 Salary Predictor",
        use_container_width=True
    ):
        st.switch_page(
            "pages/6_Salary_Predictor.py"
        )

with col2:

    if st.button(
        "🧠 Skill Analysis",
        use_container_width=True
    ):
        st.switch_page(
            "pages/5_Skill_Analysis.py"
        )

    if st.button(
        "🤖 AI Mentor",
        use_container_width=True
    ):
        st.switch_page(
            "pages/7_AI_Career_Mentor.py"
        )   

# Recent Activity
st.subheader("📜 Recent Activity")

st.info(
    "Resume analyzed for Data Scientist role"
)

st.info(
    "Salary predicted for Data Analyst role"
)

st.info(
    "Career guidance conversation started"
)

