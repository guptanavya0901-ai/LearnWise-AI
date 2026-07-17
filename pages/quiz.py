import streamlit as st

st.set_page_config(
    page_title="Skill Assessment Quiz",
    page_icon="📝"
)

st.title("📝 Skill Assessment Quiz")

score = 0

# Question 1
q1 = st.radio(
    "1. Python mainly kis liye use hoti hai?",
    [
        "Web Development",
        "AI/ML",
        "Automation",
        "All of these"
    ]
)

# Question 2
q2 = st.radio(
    "2. SQL ka use kis liye hota hai?",
    [
        "Database",
        "Video Editing",
        "Gaming",
        "Networking"
    ]
)

# Question 3
q3 = st.radio(
    "3. HTML kis liye use hota hai?",
    [
        "Website Structure",
        "Database",
        "AI",
        "Operating System"
    ]
)

# Question 4
q4 = st.radio(
    "4. CSS ka use kis liye hota hai?",
    [
        "Styling Website",
        "Database",
        "Python Coding",
        "Machine Learning"
    ]
)

# Question 5
q5 = st.radio(
    "5. JavaScript kis liye use hota hai?",
    [
        "Website Interactivity",
        "Database",
        "Operating System",
        "Compiler"
    ]
)

if st.button("Submit Quiz"):

    if q1 == "All of these":
        score += 1

    if q2 == "Database":
        score += 1

    if q3 == "Website Structure":
        score += 1

    if q4 == "Styling Website":
        score += 1

    if q5 == "Website Interactivity":
        score += 1

    st.success(f"🎯 Your Score: {score}/5")

    if score == 5:
        st.balloons()

    if score >= 4:
        st.success("Level : Advanced 🟢")
    elif score >= 2:
        st.warning("Level : Intermediate 🟡")
    else:
        st.error("Level : Beginner 🔴")

    st.subheader("🎯 Recommended Learning Path")

    if score == 5:
        st.success("Excellent! You are ready for Advanced Courses.")
        st.write("✅ Deep Learning")
        st.write("✅ Generative AI")
        st.write("✅ TensorFlow")
        st.write("✅ OpenCV")

    elif score >= 3:
        st.info("Good Job! Strengthen your concepts with these courses:")
        st.write("📘 Python Programming")
        st.write("📘 SQL")
        st.write("📘 Data Structures")
        st.write("📘 Web Development")

    else:
        st.warning("Start with beginner-level courses:")
        st.write("📗 Python Basics")
        st.write("📗 HTML & CSS")
        st.write("📗 SQL Basics")
        st.write("📗 Computer Fundamentals")

    st.progress(score / 5)