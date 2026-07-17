import streamlit as st

st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="🛣️"
)

st.title("🛣️ Personalized Learning Roadmap")

goal = st.selectbox(
    "Select Your Career Goal",
    [
        "AI Engineer",
        "Data Scientist",
        "Web Developer",
        "Cyber Security"
    ]
)

if st.button("Generate Roadmap"):

    st.subheader("📚 Your Learning Roadmap")

    if goal == "AI Engineer":

        st.success("Week 1 : Python")
        st.success("Week 2 : SQL")
        st.success("Week 3 : NumPy & Pandas")
        st.success("Week 4 : Statistics")
        st.success("Week 5 : Machine Learning")
        st.success("Week 6 : Deep Learning")
        st.success("Week 7 : Build AI Project")
        st.success("Week 8 : Interview Preparation")

    elif goal == "Data Scientist":

        st.success("Week 1 : Python")
        st.success("Week 2 : SQL")
        st.success("Week 3 : Excel & Power BI")
        st.success("Week 4 : Statistics")
        st.success("Week 5 : Machine Learning")
        st.success("Week 6 : Data Visualization")
        st.success("Week 7 : Projects")
        st.success("Week 8 : Interview Preparation")

    elif goal == "Web Developer":

        st.success("Week 1 : HTML")
        st.success("Week 2 : CSS")
        st.success("Week 3 : JavaScript")
        st.success("Week 4 : React")
        st.success("Week 5 : Node.js")
        st.success("Week 6 : MongoDB")
        st.success("Week 7 : Full Stack Project")
        st.success("Week 8 : Deployment")

    elif goal == "Cyber Security":

        st.success("Week 1 : Networking")
        st.success("Week 2 : Linux")
        st.success("Week 3 : Python")
        st.success("Week 4 : Ethical Hacking")
        st.success("Week 5 : OWASP")
        st.success("Week 6 : Penetration Testing")
        st.success("Week 7 : Security Project")
        st.success("Week 8 : Certification Preparation")