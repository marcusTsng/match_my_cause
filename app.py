import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Data retrieval from sheets database
conn = st.connection("gsheets", type=GSheetsConnection)
def get_data():
    return []

# Home page code
def home_page():
    st.title("Match My Cause")
    search = st.text_input("Search for charities")
    if search:
        data = get_data()
        if len(data) == 0: 
            st.write("No charities found")
        else:
            pass # Show the charities

# Profile page code
def profile_page():
    st.title("My Profile")
    username = st.text_input("Username:", "DefaultUsernameTest")
    st.text(f"Just for testing: Username is {username}")
    st.text("kill yourself")
    st.text("i want to have babies with andrew")

# Sidebar (menu/page selection) code
with st.sidebar:
    st.title("Menu")
    page = st.radio("MENU", ["Home", "Profile"])
    st.divider()
    st.metric(label="Charities Supported", value="12", delta="3 this week")

# Calling different pages
if page == "Home":
    home_page()
elif page == "Profile":
    profile_page()