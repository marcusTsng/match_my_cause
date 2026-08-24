import streamlit as st

with st.container(key="registerPage"):
    with st.container(key="registerTitleContainer"):
        st.markdown('<h2 class="registerTitle">Register your own charity</h2>', unsafe_allow_html=True)
        st.markdown('<h2 class="registerTitleSmall">Register</h2>', unsafe_allow_html=True)

    with st.container(key="formContainer"):
        formColumns = st.columns(2, gap='medium')
        with formColumns[0]:
            newName = st.text_input("**Charity Name**", placeholder="Tell us your charity's name")
            newCategory = st.selectbox("**Category**",
                                       ["Animals", "Environment", "Education", "Poverty", "Healthcare", "Culture", "Rights", "Other"],
                                       key="selectCategory", index=None, placeholder="Select a category", filter_mode=None)
            newTags = st.multiselect("**Tags**", [
                                        "Children",
                                        "Youth",
                                        "Elderly",
                                        "Veterans",
                                        "Women",
                                        "Refugees",
                                        "Disabilities",
                                        "Low Income",
                                        "Families",
                                        "Wildlife",
                                        "Ocean Conservation",
                                        "Climate Action",
                                        "Sustainability",
                                        "Animal Rescue",
                                        "Reforestation",
                                        "Mental Health",
                                        "Cancer Research",
                                        "Medical Care",
                                        "Addiction Recovery",
                                        "Nutrition",
                                        "Maternal Health",
                                        "Emergency Relief",
                                        "Food Bank",
                                        "Housing",
                                        "Education Access",
                                        "Legal Aid",
                                        "Clean Water",
                                        "Arts Access",
                                        "STEM Education",
                                        "Human Rights"],
                                     accept_new_options=True, placeholder="Choose or add your own tags", help="These will allow users to search for your charity.")
            newWebsite = st.text_input("**Website Link**", placeholder="Paste your website's URL")

        with formColumns[1]:
            newDesc = st.text_area("**Description**", placeholder="Tell us about your charity", height='stretch', help="This will be displayed in its entirety on your charity's page.")


        with st.container(key='submitContainer'):
            submitted = st.button("Submit", width='stretch', type='primary')
