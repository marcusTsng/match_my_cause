import streamlit as st
import dataManagement

from dataManagement import Charity

loadedCharities = dataManagement.loadCharities()

class Card:
    def __init__(self, c : Charity):
        self.id = c.ID
        self.name = c.name
        self.category = c.category
        self.status = c.status
        self.visits = c.visits
        self.donations = c.donations
        self.logoUrl = c.logoURL
        self.desc = c.description

    def display(self):
        st.title(self.name)
        st.text(self.desc)

def searchFunction(query):
    IDsFoundTitle = []
    IDsFoundTags = []
    IDsFoundDesc = []
    for charity in loadedCharities:
        for searchTerm in query:
            if searchTerm in charity.name.lower():
                IDsFoundTitle.append(charity.ID)
            elif any(searchTerm in tag for tag in charity.tags):
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
            charity : Charity = loadedCharities[int(c) - 1]
            Card(charity).display()
            # st.text(charity.name)
    else:
        st.text("No charities found")

