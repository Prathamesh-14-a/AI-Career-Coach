import streamlit as st
from src.auth.session_manager import logout

def show_sidebar():

    with st.sidebar:

        st.title("🚀 DataPilot AI")

        st.caption(
            "Navigate Your Data Career with AI"
        )

        st.divider()

        st.write(
            f"👤 {st.session_state['username']}"
        )

        st.divider()

        if st.button(
            "🚪 Logout",
            key="sidebar_logout",
            use_container_width=True
        ):
            logout()
            st.switch_page("pages/1_Login.py")