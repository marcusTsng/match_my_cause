import streamlit as st

st.set_page_config(page_title="MatchMyCause")

homePage = st.Page("views/home.py", title="Home", default=True)
discoverPage = st.Page("views/discover.py", title="Discover")
registerPage = st.Page("views/register.py", title="Register")
profilePage = st.Page("views/charity.py", title="Charity Profile")

page = st.navigation({
    "Main": [homePage, discoverPage, registerPage],
    "Hidden": [profilePage]
})

pg.run()
