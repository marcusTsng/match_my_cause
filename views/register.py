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

        st.space(size=1)
        st.write("**Upload Images**")

        pictureColumns = st.columns(6, gap='medium')

        newImages = [None] * 6

        for newImageInd in range(6):
            if f"newImage{newImageInd}" not in st.session_state:
                st.session_state[f"newImage{newImageInd}"] = False
            if f"resetImage{newImageInd}" not in st.session_state:
                st.session_state[f"resetImage{newImageInd}"] = False

        for columnIndex in range(6):
            with pictureColumns[columnIndex]:
                if columnIndex == 0:
                    label = "Logo"
                else:
                    label = f"Image {columnIndex}"

                if st.session_state[f"newImage{columnIndex}"]:
                    st.html(f"""
                        <style>
                        .imageUpload{columnIndex}""" + """ {
                            background: red;
                            display: none;
                        }
                        </style>""")

                with st.container(key=f"imageUploadContainer{columnIndex}"):
                    if st.session_state[f"resetImage{columnIndex}"]:
                        st.session_state[f"toReset{columnIndex}"] = ""
                        st.session_state[f"resetImage{columnIndex}"] = False

                    with st.popover(f"**{label}**", key=f"imageUpload{columnIndex}", type='tertiary'):
                        newImages[columnIndex] = st.text_input(f"{label} URL", key=f"toReset{columnIndex}")
                        if newImages[columnIndex] and not st.session_state[f"newImage{columnIndex}"]:
                            st.session_state[f"newImage{columnIndex}"] = True
                            st.rerun()

                    if newImages[columnIndex]:
                        with st.container(key=f"uploadedImage{columnIndex}"):
                            st.image(newImages[columnIndex])
                            if st.button("Remove", key=f"removeImage{columnIndex}", width='stretch', type='tertiary'):
                                newImages[columnIndex] = None
                                st.session_state[f"newImage{columnIndex}"] = False
                                st.session_state[f"resetImage{newImageInd}"] = True
                                st.rerun()


        with st.container(key='submitContainer'):
            submitted = st.button("Submit", width='stretch', type='primary')
