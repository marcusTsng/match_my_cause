import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()

visits = []
for listID in range(len(loadedCharities)):
    visits.append([listID, loadedCharities[listID].visits])

numTrending = 3
trendingCharities = sorted(visits, key=lambda x: x[1], reverse=True)[:numTrending]


with st.container(key="logoBar"):
    barColumns = st.columns(2)
    with barColumns[0]:
        st.image(
            "images/MatchMyCause Text White.svg",
            width="content"
        )
    with barColumns[1]:
        if st.button(":material/search: Discover", key="searchButton", type="tertiary"):
            st.switch_page("views/discover.py")


with st.container(key="trendingCarousel"):
    st.markdown('<h2 class="trendingHeader">Trending Charities</h2>', unsafe_allow_html=True)

    htmlCarousel = '<div class="charityFlexRow">'

    for trending in trendingCharities:
        charity = loadedCharities[trending[0]]
        id = int(charity.ID)
        htmlCarousel += (
        f'<div class="charityCard">'
        f'<img src="{charity.logoURL}" class="cardImage" alt="{charity.name}">'
        f'<div class="cardContent">'
        f'<div class="cardBody">'
        f'<span class="cardTag">{charity.category}</span>'
        f'<h4 class="cardTitle">{charity.name}</h4>'
        f'<p class="cardDesc">{dataManagement.truncateString(charity.description,100)}</p>'
        f'</div>'
        f'<div class="learnMore">'
        f'<a href="/charity?id={id}" target="_self" class="cardLink">Learn More</a>'
        f'</div>'
        f'</div>'
        f'</div>'
        )

    htmlCarousel += "</div>"
    st.markdown(htmlCarousel, unsafe_allow_html=True)



# Search bar
if "searchBarData" not in st.session_state:
    st.session_state["searchBarData"] = ""
with st.container(key="searchBarContainer"):
    searchTerm = st.text_input("", icon=":material/search:", placeholder="Search for charities...", key="searchBar")
    if searchTerm:
        st.session_state["searchBarData"] = searchTerm
        st.switch_page("views/discover.py")


with st.container(key="aboutUs", border=True):
    st.title("About Us")

    aboutColumns1 = st.columns([6,4], gap="medium")
    with aboutColumns1[0]:
        st.header("Interesting things")
        st.write("This is something interesting about us")
    with aboutColumns1[1]:
        st.space("xxsmall")
        with st.container(border=True, key="aboutUsImage1"):
            st.write("This is an image with a fixed aspect ratio of 4:3")

    st.divider()

    aboutColumns2 = st.columns([2, 8], gap="medium")
    with aboutColumns2[0]:
        st.space("xxsmall")
        with st.container(border=True, key="aboutUsImage2"):
            st.write("This is a portrait, 3:4")
    with aboutColumns2[1]:
        st.header("Author 1")
        st.write("This is something about one author")


    st.divider()

    aboutColumns3 = st.columns([8, 2], gap="medium")
    with aboutColumns3[0]:
        st.header("Author 2")
        st.write("This is something about another author")
    with aboutColumns3[1]:
        st.space("xxsmall")
        with st.container(border=True, key="aboutUsImage3"):
            st.write("This is a portrait, 3:4")

    st.space("xsmall")
