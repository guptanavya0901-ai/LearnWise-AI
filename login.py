import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Login")

st.write("Welcome to LearnWise AI")

email = st.text_input("📧 Email")

password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    if email == "" or password == "":
        st.error("Please fill all fields.")
    else:
        st.success("Login Successful!")