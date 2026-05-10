# OI OI OI 

# THIS IS JUST THE PROTOTYPE TEST THING DONT PUT THE CODE FOR THE ACTUAL APP IN HERE ITS GONNA BE DELELETED LATER



import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn = st.connection("gsheets", type=GSheetsConnection)

with st.sidebar:
    st.title("Menu")
    page = st.radio("MENU", ["Home", "My Charities"])
    st.divider()
    st.metric(label="Charities Supported", value="12", delta="3 this week")

if page == "Home":
    st.header("Home page")
    
    # Logic for posting
    if prompt := st.chat_input("What's on your mind?"):
        # Read existing data and ignore empty rows at the bottom of the sheet
        existing_data = conn.read(worksheet="Sheet1", ttl=0).dropna(how="all")
        
        new_row = pd.DataFrame([{"User": "USERTEST", "Message": prompt}])
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        
        # Update the default sheet
        conn.update(worksheet="Sheet1", data=updated_df)
        st.success("Posted!")
        st.rerun()

    st.divider()

    # Display the Feed
    try:
        existing_posts = conn.read(worksheet="Sheet1", ttl=0).dropna(how="all")
        
        if not existing_posts.empty:
            # Display rows in reverse order (newest first)
            for index, row in existing_posts.iloc[::-1].iterrows():
                with st.chat_message("user"):
                    user = row.get("User", "Unknown")
                    msg = row.get("Message", "")
                    st.write(f"**{user}**: {msg}")
    except Exception as e:
        st.error(f"Waiting for database connection... {e}")

elif page == "My Charities":
    st.header("My Charities")
    st.write("Your followed charities will appear here.")