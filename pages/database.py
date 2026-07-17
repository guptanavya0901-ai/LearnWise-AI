import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Database",
    page_icon="🗄️"
)

st.title("🗄️ Student Database")

# Database Connection
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    skill TEXT
)
""")
conn.commit()

st.header("➕ Add Student")

name = st.text_input("Name")
email = st.text_input("Email")
skill = st.text_input("Skill")

if st.button("Save"):
    cursor.execute(
        "INSERT INTO students(name,email,skill) VALUES(?,?,?)",
        (name, email, skill)
    )
    conn.commit()
    st.success("Student Saved Successfully!")

st.markdown("---")

st.header("📋 Student Records")

df = pd.read_sql("SELECT * FROM students", conn)

st.dataframe(df)