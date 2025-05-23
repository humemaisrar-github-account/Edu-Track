import streamlit as st
from models.user import User

def login():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Username", key="username_input")
    role = st.sidebar.radio("Login as", options=["teacher", "parent"], key="role_radio")

    if username:
        return User(username=username, role=role)
    else:
        return User(username="guest", role="parent")
