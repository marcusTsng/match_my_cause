import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()


def searchFunction(query):
    IDsFoundTitle = []
    IDsFoundCats = []
    IDsFoundTags = []
    IDsFoundDesc = []
    for searched in loadedCharities:
        for searchTerm in query:
            if searchTerm in searched.name.lower():
                IDsFoundTitle.append(searched.ID)
            elif searchTerm in searched.category.lower():
                IDsFoundCats.append(searched.ID)
            elif any(searchTerm in tag for tag in searched.tags):
                IDsFoundTags.append(searched.ID)
            elif searchTerm in searched.description.lower():
                IDsFoundDesc.append(searched.ID)

    return IDsFoundTitle + IDsFoundCats + IDsFoundTags + IDsFoundDesc

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

with st.container(key="searchContainer", height=140):
    searchQuery = st.text_input("", searchContents, icon=":material/search:", placeholder="Search names, tags, categories...", key="searchBox")

if searchQuery or searchContents:
    charities = searchFunction(searchQuery.lower().split(" "))
    if len(charities) > 0:
        with st.container(key="searchResults"):
            charitiesToShow = []
            for loadCharity in loadedCharities:
                if loadCharity.ID in charities:
                    charitiesToShow.append(loadCharity)

            containerID = 1
            for charity in charitiesToShow:
                with st.container(key=f"foundCharity{containerID}"):
                    displayColumns = st.columns([3,7])
                    with displayColumns[0]:
                        with st.container(key=f"charityImage{containerID}"):
                            st.image(charity.logoURL, width="stretch")
                    with displayColumns[1]:
                        st.write("This is a description")

                containerID += 1
    else:
        with st.container(key="noResults"):
            with st.container(key="noResultsBoth"):
                with st.container(key="noResultsIcon"):
                    st.write(":material/search_off:")
                with st.container(key="noResultsMessage"):
                    st.write("No charities found")
else:
        with st.container(key="noResults"):
            with st.container(key="noResultsIcon"):
                st.write(":material/search:")
            with st.container(key="noResultsMessage"):
                st.write("Search anything!")
