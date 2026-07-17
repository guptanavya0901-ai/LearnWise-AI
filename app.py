import streamlit as st

st.set_page_config(
    page_title="LearnWise AI",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 LearnWise AI")
st.subheader("Intelligent Recommendation System for E-Learning Platforms")

st.markdown("---")

st.header("📖 About Project")

st.write("""
LearnWise AI is an AI-powered E-Learning Recommendation System.

It helps students by:
- 🎯 Recommending personalized courses
- 📄 Analyzing resumes
- 📝 Conducting skill assessment quizzes
- 🛣️ Generating learning roadmaps
- 🤖 Providing AI career guidance
""")

st.markdown("---")

st.header("🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("📄 Resume Upload")
    st.success("📝 Skill Assessment Quiz")
    st.success("🎯 AI Course Recommendation")

with col2:
    st.success("🛣️ Learning Roadmap")
    st.success("📊 Progress Dashboard")
    st.success("🤖 AI Career Chatbot")

st.markdown("---")

if st.button("🚀 Get Started"):
    st.success("Select a page from the left sidebar to begin.")