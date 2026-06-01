import streamlit as st


st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer")
st.write("Upload your resume for ATS analysis")


uploaded_file = st.file_uploader(
    label="Upload Resume (PDF only)",
    type=["pdf"]
)


if uploaded_file is not None:
    file_details = {
        "Filename": uploaded_file.name,
        "File size": f"{uploaded_file.size / 1024:.2f} KB",
        "File type": uploaded_file.type
    }

    st.success("Resume uploaded successfully!")

    st.subheader("Uploaded File Details")

    for key, value in file_details.items():
        st.write(f"**{key}:** {value}")