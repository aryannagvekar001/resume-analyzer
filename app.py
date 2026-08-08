import streamlit as st

from analyzer.resume_parser import extract_resume_text
from analyzer.analyzer import detect_skills, calculate_resume_score


st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and get an instant analysis of "
    "skills, structure and resume quality."
)


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


if uploaded_file:

    st.success(f"Uploaded: {uploaded_file.name}")

    try:

        resume_text = extract_resume_text(uploaded_file)

        if not resume_text.strip():
            st.error("Could not extract text from this resume.")
            st.stop()

        st.subheader("📋 Resume Preview")

        with st.expander("Show extracted text"):
            st.text(resume_text[:5000])

        score = calculate_resume_score(resume_text)

        skills = detect_skills(resume_text)

        st.subheader("📊 Resume Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Resume Score",
                f"{score}/100"
            )

        with col2:
            st.metric(
                "Skills Detected",
                len(skills)
            )

        st.subheader("🛠️ Detected Skills")

        if skills:

            for skill in skills:
                st.write(f"✅ {skill}")

        else:
            st.warning("No common technical skills detected.")

    except Exception as e:

        st.error(f"Error: {e}")