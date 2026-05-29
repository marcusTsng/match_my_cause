import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# Class for all charities
class Charity:
    def __init__(self, ID, name, category, status, tags, website, logoURL, description):
        self.ID = ID
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
        ID=row['ID'],
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


def uploadToSheet(name, category, tags, website, logoURL, description):
    currentState = conn.read(worksheet="Sheet1", ttl=0).dropna(how='all')

    # Assigns a new ID (if rows are deleted, their IDs won't be replaced)
    if currentState.empty or "ID" not in currentState.columns:
        nextID = 1
    else:
        nextID = int(pd.to_numeric(currentState["ID"], errors='coerce').max()) + 1

    toUpload = {
        'ID': nextID,
        'Name': name,
        'Category': category,
        'Status': "Pending",
        'Tags': tags,  # Separated by commas (please)
        'Website': website,
        'LogoURL': logoURL,
        'Description': description
    }

    updatedState = pd.concat([currentState, pd.DataFrame([toUpload])], ignore_index=True)
    conn.update(worksheet="Sheet1", data=updatedState)

    st.cache_data.clear() # Ensures the website updates after uploading


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