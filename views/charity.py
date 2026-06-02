import streamlit as st

parameters = st.query_params

if "id" in parameters:
    charityId = int(parameters['id'])
else:
    st.warning("None")