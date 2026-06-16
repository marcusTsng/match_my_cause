import streamlit as st
from dataManagement import injectCSS

st.set_page_config(page_title="MatchMyCause", layout='wide', page_icon="images/MatchMyCause Icon.svg")

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


with st.container(key="logo"):
    try:
        with open("images/MatchMyCause Logo.svg", "r") as f:
            svgCode = f.read()
        st.markdown(
            f'<a href="/" target="_top">'
            f'  {svgCode}'
            f'</a>',
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        st.error("Logo file not found")


injectCSS()

page.run()
