import streamlit as st
from views.home import loadedCharities


def searchFunction(query):
    IDsFoundTitle = []
    IDsFoundTags = []
    IDsFoundDesc = []
    for charity in loadedCharities:
        for searchTerm in query:
            if searchTerm in charity.title:
                IDsFoundTitle.append(charity.ID)
            elif searchTerm in charity.tags:
                IDsFoundTags.append(charity.ID)
            elif searchTerm in charity.description:
                IDsFoundDesc.append(charity.ID)

    return IDsFoundTitle + IDsFoundTags + IDsFoundDesc
