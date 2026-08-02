import streamlit as st
import dataManagement

parameters = st.query_params

if "id" in parameters:
    charityId = int(parameters['id'])

    dataManagement.charityVisited(charityId)
else:
    st.warning("No ID provided.")