import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()


with st.container(key="logoCard"):
    st.image(
        "images/MatchMyCause Text White.svg",
        use_container_width=True
    )


# Search bar
if "searchBarData" not in st.session_state:
    st.session_state["searchBarData"] = ""
with st.container(key="searchBar"):
    searchTerm = st.text_input("", placeholder="Search for charities...")
    if searchTerm:
        st.session_state["searchBarData"] = searchTerm
        st.switch_page("views/discover.py")

with st.container(key="aboutUs", height=1000):
    st.write("About us...")