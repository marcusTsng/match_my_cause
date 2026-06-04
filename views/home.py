import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()

with st.container(key="blueContainer_1"):
    st.write("test")

# Session data
if "searchBarData" not in st.session_state:
    st.session_state["searchBarData"] = ""

# Search bar
searchTerm = st.text_input("", placeholder="Search for charities...")
if searchTerm:
    st.session_state["searchBarData"] = searchTerm
    st.switch_page("views/discover.py")
