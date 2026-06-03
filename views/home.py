import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()

with st.container(key="blueContainer_1"):
    st.write("test")

# Session data
if "search_bar_data" not in st.session_state:
    st.session_state["search_bar_data"] = ""

# Search bar
search_term = st.text_input("Search for charities...", "")
if search_term:
    st.session_state["search_bar_data"] = search_term
    st.switch_page("views/discover.py")