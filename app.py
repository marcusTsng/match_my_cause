import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# Possible categories:
# - Animals
# - Environment
# - Inclusion
# - Education
# - Health
# - Poverty
#
# Tags will effectively work as our search engine


# Class for all charities
class Charity:
    def __init__(self, name, category, status, tags, website, logoURL, description):
        self.name = name
        self.category = category
        self.status = status
        self.tags = tags
        self.website = website
        self.logoURL = logoURL
        self.description = description


# Data retrieval from Sheets database
conn = st.connection("gsheets", type=GSheetsConnection)
charitiesLoaded = conn.read(worksheet="Sheet1", ttl=60).dropna(how='all')
allCharities = []
for index, row in charitiesLoaded.iterrows():
    tagList = [
        tag.strip().lower()
        for tag in str(row['Tags']).split(',')
        if tag.strip() and str(row['Tags']) != 'nan'
    ]

    individual_charity = Charity(
        name=row['Name'],
        category=row['Category'],
        status=row['Status'],
        tags=tagList,
        website=row['Website'],
        logoURL=row['LogoURL'],
        description=row['Description']
    )
    allCharities.append(individual_charity)

# allCharities should now hold all charities within the database as objects in the Charity class.

print([charity.name for charity in allCharities]) # Debug


def uploadToSheet(name, category, tags, website, logoURL, description):
    toUpload = {
        'name': name,
        'category': category,
        'status': "Pending",
        'tags': tags, # Separated by commas (please)
        'website': website,
        'logoURL': logoURL,
        'description': description
    }

    currentState = conn.read(worksheet="Sheet1", ttl=0).dropna(how='all')
    updatedState = pd.concat([currentState, toUpload], ignore_index=True)
    conn.update(worksheet="Sheet1", data=updatedState)

    st.cache_data.clear()
    st.rerun() # Ensures the website updates after uploading


# Home page code
def homePage():
    st.title("Match My Cause")
    # search = st.text_input("Search for charities")
    # if search:
    #     data = get_data()
    #     if len(data) == 0:
    #         st.write("No charities found")
    #     else:
    #         pass # Show the charities

# Profile page code
def profilePage():
    st.title("My Profile")
    username = st.text_input("Username:", "DefaultUsernameTest")
    st.text(f"Just for testing: Username is {username}")

# Sidebar (menu/page selection) code
with st.sidebar:
    st.title("Menu")
    page = st.radio("MENU", ["Home", "Profile"])
    st.divider()
    st.metric(label="Charities Supported", value="12", delta="3 this week")

# Calling different pages
if page == "Home":
    homePage()
elif page == "Profile":
    profilePage()