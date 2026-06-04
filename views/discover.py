import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()


def searchFunction(query):
    IDsFoundTitle = []
    IDsFoundTags = []
    IDsFoundDesc = []
    for charity in loadedCharities:
        for searchTerm in query:
            if searchTerm in charity.name.lower():
                IDsFoundTitle.append(charity.ID)
            elif searchTerm in [tag.lower() for tag in charity.tags]:
                IDsFoundTags.append(charity.ID)
            elif searchTerm in charity.description.lower():
                IDsFoundDesc.append(charity.ID)

    return IDsFoundTitle + IDsFoundTags + IDsFoundDesc

# Search bar
if "searchBarData" in st.session_state:
    searchContents = st.session_state["searchBarData"]
    st.session_state["searchBarData"] = ""
else:
    searchContents = ""

searchQuery = st.text_input("", searchContents, placeholder="Search for charities")
if searchQuery or searchContents:
    charities = searchFunction(searchQuery.lower().split(" "))
    if len(charities) > 0:
        for c in charities:
            st.text(c)
    else:
        st.text("No charities found")
