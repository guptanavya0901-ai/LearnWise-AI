import streamlit as st

st.set_page_config(page_title="Profile", page_icon="👤")

st.title("👤 Student Profile")

name = st.text_input("Full Name")
email = st.text_input("Email")

age = st.number_input("Age", min_value=10, max_value=60)

education = st.selectbox(
    "Education",
    ["B.Tech", "BCA", "MCA", "B.Sc", "Other"]
)

goal = st.selectbox(
    "Career Goal",
    [
        "AI Engineer",
        "Data Scientist",
        "Web Developer",
        "App Developer",
        "Cyber Security",
        "Cloud Engineer"
    ]
)

skills = st.text_area(
    "Current Skills",
    placeholder="Example: Python, HTML, CSS"
)

if st.button("Save Profile"):
    st.success("✅ Profile Saved Successfully!")