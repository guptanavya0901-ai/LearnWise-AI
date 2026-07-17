import streamlit as st
import fitz

st.set_page_config(
    page_title="Resume Parser",
    page_icon="📄"
)

st.title("📄 Resume Parser")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    st.success("✅ Resume Uploaded Successfully!")

    st.subheader("📄 Resume Content")
    st.write(text)

    st.subheader("🛠 Extracted Skills")

    skills = [
        "Python",
        "C",
        "C++",
        "Java",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Excel",
        "Power BI",
        "Machine Learning",
        "AI",
        "React",
        "MongoDB",
        "Flask",
        "FastAPI"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    if found_skills:
        for skill in found_skills:
            st.success(skill)
    else:
        st.warning("No skills detected.")