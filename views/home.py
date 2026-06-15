import streamlit as st
import dataManagement
from dataManagement import truncateString

loadedCharities = dataManagement.loadCharities()


with st.container(key="logoBar"):
    st.image(
        "images/MatchMyCause Text White.svg",
        width="content"
    )


with st.container(key="trendingCarousel"):
    st.header("Trending Charities")

    htmlCarousel = '<div class="charityFlexRow">'

    for charity in loadedCharities:
        id = int(charity.ID)
        htmlCarousel += (
        f'<div class="charityCard">'
        f'<img src="{charity.logoURL}" class="cardImage" alt="{charity.name}">'
        f'<div class="cardContent">'
        f'<div class="cardBody">'
        f'<span class="cardTag">{charity.category}</span>'
        f'<h4 class="cardTitle">{charity.name}</h4>'
        f'<p class="cardDesc">{truncateString(charity.description,100)}</p>'
        f'</div>'
        f'<div class="learnMore">'
        f'<a href="/charity?id={id}" target="_self" class="cardLinkButton">Learn More</a>'
        f'</div>'
        f'</div>'
        f'</div>'
        )

    htmlCarousel += "</div>"
    st.markdown(htmlCarousel, unsafe_allow_html=True)



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