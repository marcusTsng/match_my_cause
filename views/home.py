import streamlit as st
import dataManagement

loadedCharities = dataManagement.loadCharities()

with st.container(key="blueContainer_1"):
    st.write("test")
