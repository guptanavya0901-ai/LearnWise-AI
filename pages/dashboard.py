import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("📊 LearnWise AI Dashboard")

conn = sqlite3.connect("students.db")
df = pd.read_sql("SELECT * FROM students", conn)

if df.empty:
    st.warning("No student data available.")
else:

    # ===== Metrics =====
    total_students = len(df)
    total_skills = df["skill"].nunique()
    top_skill = df["skill"].value_counts().idxmax()

    col1, col2, col3 = st.columns(3)

    col1.metric("👨‍🎓 Students", total_students)
    col2.metric("💻 Skills", total_skills)
    col3.metric("🏆 Top Skill", top_skill)

    st.divider()

    # ===== Student Table =====
    st.subheader("📋 Student Records")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # ===== Search =====
    search = st.text_input("🔍 Search Student")

    if search:
        result = df[df["name"].str.contains(search, case=False)]
        st.dataframe(result, use_container_width=True)

    st.divider()

    # ===== Charts =====
    skill_count = df["skill"].value_counts()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Bar Chart")

        fig, ax = plt.subplots(figsize=(5,4))
        ax.bar(skill_count.index, skill_count.values)
        ax.set_xlabel("Skill")
        ax.set_ylabel("Students")
        st.pyplot(fig)

    with col2:
        st.subheader("🥧 Pie Chart")

        fig2, ax2 = plt.subplots(figsize=(5,4))
        ax2.pie(
            skill_count.values,
            labels=skill_count.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax2.axis("equal")
        st.pyplot(fig2)

    st.success("✅ Dashboard Updated Successfully!")