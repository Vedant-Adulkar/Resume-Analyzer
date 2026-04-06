import streamlit as st
from pypdf import PdfReader
from multi_agent_system import run_resume_analysis

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer (Multi-Agent System)")

# JD Input
jd = st.text_area("Enter Job Description")

# PDF Upload
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Button
if st.button("Analyze Resume"):
    if not jd or not uploaded_file:
        st.warning("Please provide both JD and Resume PDF")
    else:
        resume_text = extract_text_from_pdf(uploaded_file)

        with st.spinner("Analyzing..."):
            result = run_resume_analysis(jd, resume_text)

        st.subheader("📊 Score")
        st.success(result["score"])

        st.subheader("💡 Suggestions")
        st.info(result["suggestions"])

        st.subheader("🚀 Project Suggestions")
        st.markdown(result["project_suggestions"])