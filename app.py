import streamlit as st
from dataManagement import injectCSS

st.set_page_config(page_title="MatchMyCause", layout='wide')

homePage = st.Page("views/home.py", title="Home", default=True)
discoverPage = st.Page("views/discover.py", title="Discover")
registerPage = st.Page("views/register.py", title="Register")
profilePage = st.Page("views/charity.py", title="Charity Profile")

page = st.navigation([
    homePage,
    discoverPage,
    registerPage,
    profilePage
], position="hidden")

injectCSS()

page.run()
