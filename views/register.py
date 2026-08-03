import streamlit as st

with st.container(key="registerPage"):
    with st.container(key="registerTitleContainer"):
        st.markdown('<h2 class="registerTitle">Register your own charity</h2>', unsafe_allow_html=True)
        st.markdown('<h2 class="registerTitleSmall">Register</h2>', unsafe_allow_html=True)

    with st.container(key="formContainer"):
        with st.form(key="registerCharity", clear_on_submit=True, enter_to_submit=False):
            formColumns = st.columns(2, gap='medium')
            with formColumns[0]:
                newName = st.text_input("**Charity Name**", placeholder="Tell us your charity's name!")
                newCategory = st.selectbox("**Category**",
                                           ["Animals", "Environment", "Education", "Poverty", "Healthcare", "Culture", "Rights", "Other"],
                                           key="selectCategory", index=None, placeholder="Select a category", filter_mode=None)
                newTags = st.multiselect("**Tags**", [""])

            with formColumns[1]:
                newDes = st.text_area("**Description**", height='stretch')

            with st.container(key='submitContainer'):
                submitted = st.form_submit_button("Submit", width='stretch', type='primary')
