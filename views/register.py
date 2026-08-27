import streamlit as st

import dataManagement

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
                                     accept_new_options=True, placeholder="Choose or add your own tags",
                                     help="These will allow users to search for your charity.", max_selections=10)
            newWebsite = st.text_input("**Website Link**", placeholder="Paste your website's URL")
            newDonation = st.text_input("**Donation Link**", placeholder="Paste a link that allows people to donate",
                                        help="If you don't have a specific link, or this doesn't apply to your charity, use your website URL.")

        with formColumns[1]:
            newDesc = st.text_area("**Description**", placeholder="Tell us about your charity", height='stretch', help="This will be displayed in its entirety on your charity's page.")

        st.markdown("**Images** -- Upload a logo and up to five images.")
        imageColumns = st.columns(6, gap='small')
        uploadedImages = [None] * 6
        print(uploadedImages)
        for columnID in range(6):
            with imageColumns[columnID]:
                if columnID == 0:
                    imageName = "**Logo**"
                elif columnID == 1:
                    imageName = f"**Image {columnID}**"
                else:
                    imageName = f"**Image {columnID}** -- Optional"
                with st.container(key=f"imageContainer{columnID}"):
                    st.markdown(imageName)
                    newImage = st.text_input("Image URL", label_visibility="hidden", key=f"uploadImageURL{columnID}", placeholder="Paste an image URL")
                    with st.container(key=f"uploadedImage{columnID}"):
                        try:
                            st.image(newImage)
                            uploadedImages[columnID] = newImage
                        except:
                            st.skeleton(height="stretch")
        print(uploadedImages)

        with st.container(key='submitContainer'):
            submitted = st.button("Submit", width='stretch', type='primary')
            if submitted:
                if all([newName, newCategory, newTags, newWebsite, newDonation, uploadedImages[0], uploadedImages[1]]):
                    uploadTags = ", ".join(newTags)
                    dataManagement.uploadToSheet(newName, newCategory, uploadTags, newWebsite, newDonation, *uploadedImages, newDesc)
                else:
                    st.toast("Please ensure that all fields have been filled out, and that your Logo and Image 1 are displaying properly.")
