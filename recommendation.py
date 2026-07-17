import streamlit as st

st.set_page_config(page_title="AI Recommendation", page_icon="🤖")

st.title("🤖 Intelligent Course Recommendation System")
st.write("Select your skills and career goal to get personalized recommendations.")

skills = st.multiselect(
    "Choose Your Skills",
    [
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
        "Machine Learning"
    ]
)

goal = st.selectbox(
    "Career Goal",
    [
        "AI Engineer",
        "Data Scientist",
        "Web Developer",
        "Cyber Security"
    ]
)

if st.button("🚀 Generate Recommendation"):

    st.progress(100)
    st.balloons()

    recommendations = []

    if "Python" in skills:
        recommendations += [
            "Pandas",
            "NumPy",
            "Machine Learning",
            "Scikit-Learn"
        ]

    if "HTML" in skills or "CSS" in skills:
        recommendations += [
            "Bootstrap",
            "React JS",
            "Node.js"
        ]

    if "Java" in skills:
        recommendations += [
            "Spring Boot",
            "Hibernate"
        ]

    if "SQL" not in skills:
        recommendations.append("Learn SQL")

    if goal == "AI Engineer":
        recommendations += [
            "Deep Learning",
            "TensorFlow",
            "OpenCV",
            "Generative AI"
        ]

    elif goal == "Data Scientist":
        recommendations += [
            "Statistics",
            "Power BI",
            "Data Visualization",
            "Python for Data Science"
        ]

    elif goal == "Web Developer":
        recommendations += [
            "React",
            "Node.js",
            "MongoDB"
        ]

    elif goal == "Cyber Security":
        recommendations += [
            "Ethical Hacking",
            "Network Security",
            "Linux"
        ]

    st.subheader("📚 Personalized Recommendations")

    for course in recommendations:
        st.success(course)

    st.subheader("🛣️ Suggested Learning Roadmap")

    if goal == "AI Engineer":
        st.info("""
1️⃣ Python Basics

⬇️

2️⃣ NumPy & Pandas

⬇️

3️⃣ Machine Learning

⬇️

4️⃣ Deep Learning

⬇️

5️⃣ TensorFlow

⬇️

6️⃣ Build AI Projects
""")

    elif goal == "Data Scientist":
        st.info("""
1️⃣ Python

⬇️

2️⃣ SQL

⬇️

3️⃣ Statistics

⬇️

4️⃣ Power BI

⬇️

5️⃣ Machine Learning

⬇️

6️⃣ Real-world Projects
""")

    st.success("🎉 Best of Luck! Keep Learning and Keep Growing.")
    