import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# Class for all charities
class Charity:
    def __init__(self, ID, name, category, status, visits, tags, website, logoURL, donationURL, image1URL, image2URL, image3URL, image4URL, image5URL, description):
        self.ID = ID
        self.name = name
        self.category = category
        self.status = status
        self.visits = visits
        self.tags = tags
        self.website = website
        self.logoURL = logoURL
        self.donationURL = donationURL
        self.image1URL = image1URL
        self.image2URL = image2URL
        self.image3URL = image3URL
        self.image4URL = image4URL
        self.image5URL = image5URL
        self.description = description


# Data retrieval from Sheets database
conn = st.connection("gsheets", type=GSheetsConnection)
@st.cache_data(ttl=120, show_spinner=False)
def loadCharities():
    allCharities = []
    charitiesLoaded = conn.read(worksheet="Sheet1", ttl=60).dropna(how='all')
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
            visits=row['Visits'],
            tags=tagList,
            website=row['Website'],
            logoURL=row['LogoURL'],
            donationURL=row['DonationURL'],
            image1URL=row['Image1URL'],
            image2URL=row['Image2URL'],
            image3URL=row['Image3URL'],
            image4URL=row['Image4URL'],
            image5URL=row['Image5URL'],
            description=row['Description']
        )
        allCharities.append(individual_charity)
    return allCharities


def uploadToSheet(name, category, tags, website, logoURL, donationURL, image1URL, image2URL, image3URL, image4URL, image5URL, description):
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
        'Visits': 0,
        'Tags': tags,  # Separated by commas (please)
        'Website': website,
        'LogoURL': logoURL,
        'DonationURL': donationURL,
        'Image1URL': image1URL,
        'Image2URL': image2URL,
        'Image3URL': image3URL,
        'Image4URL': image4URL,
        'Image5URL': image5URL,
        'Description': description
    }

    updatedState = pd.concat([currentState, pd.DataFrame([toUpload])], ignore_index=True)
    conn.update(worksheet="Sheet1", data=updatedState)

    st.cache_data.clear() # Ensures the website updates after uploading
    

def injectCSS():
    # Reads styles.css and injects styles into the main app; use key=... to select a style
    with open("styles.css", "r") as styles:
        css = styles.read()
    st.html(f"<style>{css}</style>")


@st.cache_data(ttl="1h", show_spinner=False) # Limits each user to one visit per charity per hour
def charityVisited(charityID):
    # Adds 1 to the visit count of the requested charity
    currentState = conn.read(worksheet="Sheet1", ttl=0).dropna(how='all')

    if not currentState.empty and "ID" in currentState.columns:
        mask = currentState['ID'] == charityID
        if mask.any():
            currentState.loc[mask, 'Visits'] = pd.to_numeric(currentState.loc[mask, 'Visits'], errors='coerce').fillna(
                0) + 1

            conn.update(worksheet="Sheet1", data=currentState)
