import streamlit as st
from views.home import loadedCharities


def searchFunction(query):
    IDsFoundTitle = []
    IDsFoundTags = []
    IDsFoundDesc = []
    for charity in loadedCharities:
        for searchTerm in query:
            if searchTerm in charity.name:
                IDsFoundTitle.append(charity.ID)
            elif searchTerm in charity.tags:
                IDsFoundTags.append(charity.ID)
            elif searchTerm in charity.description:
                IDsFoundDesc.append(charity.ID)

    return IDsFoundTitle + IDsFoundTags + IDsFoundDesc


'''This is the discover page'''

# Search bar
search_contents = ""

if "search_bar_data" in st.session_state:
    search_contents = st.session_state["search_bar_data"]
else: 
    st.session_state["search_bar_data"] = ""

searchTerm = st.text_input("Search for charities...", search_contents)
if searchTerm:
    charities = searchFunction(searchTerm.split(" "))
    for c in charities:
        st.text(c)