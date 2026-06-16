import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()


def searchFunction(query):
    IDsFoundTitle = []
    IDsFoundTags = []
    IDsFoundDesc = []
    for searched in loadedCharities:
        for searchTerm in query:
            if searchTerm in searched.name.lower():
                IDsFoundTitle.append(searched.ID)
            elif any(searchTerm in tag for tag in searched.tags):
                IDsFoundTags.append(searched.ID)
            elif searchTerm in searched.description.lower():
                IDsFoundDesc.append(searched.ID)

    return IDsFoundTitle + IDsFoundTags + IDsFoundDesc

with st.container(key="logoBar"):
    st.image(
        "images/MatchMyCause Discover.svg",
        width="content"
    )


# Search bar
if "searchBarData" in st.session_state:
    searchContents = st.session_state["searchBarData"]
    st.session_state["searchBarData"] = ""
else:
    searchContents = ""

with st.container(key="searchContainer", height=150):
    searchQuery = st.text_input("", searchContents, placeholder="Search names, tags, categories...", key="searchBox")

with st.container(key="searchResults"):
    if searchQuery or searchContents:
        charities = searchFunction(searchQuery.lower().split(" "))
        if len(charities) > 0:
            charitiesToShow = []
            for loadCharity in loadedCharities:
                if loadCharity.ID in charities:
                    charitiesToShow.append(loadCharity)

            containerID = 1
            for charity in charitiesToShow:
                with st.container(key=f"foundCharity{containerID}"):
                    st.write(charity.name)
                containerID += 1
        else:
            st.write(":material/search_off: No charities found")
    else:
        st.write("Search anything!")


