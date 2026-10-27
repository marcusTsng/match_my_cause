import streamlit as st
import dataManagement

parameters = st.query_params

if "id" in parameters: 
    charityId = int(parameters['id'])
    charities = dataManagement.loadCharities()
    charity = None
    for x in charities:
        x : dataManagement.Charity 
        if x.ID == charityId:
            charity : dataManagement.Charity = x
    if not charity:
        st.space("large")
        st.warning("Error - Charity not found", icon="⚠️")
    else:
        st.set_page_config(page_title=charity.name)

        with st.container(key="logoBar"):
            barColumns = st.columns(2)
            with barColumns[0]:
                st.image(
                    "images/MatchMyCause Text White.svg",
                    width="content"
                )
            with barColumns[1]:
                if st.button(":material/close:", key="searchButton", type="tertiary"):
                    st.switch_page("views/discover.py")

        carouselImages = [charity.image1URL]
        if charity.image2URL != "":
            carouselImages.append(charity.image2URL)
        if charity.image3URL != "":
            carouselImages.append(charity.image3URL)
        if charity.image4URL != "":
            carouselImages.append(charity.image4URL)
        if charity.image5URL != "":
            carouselImages.append(charity.image5URL)

        if 'carouselInd' not in st.session_state:
            st.session_state.carouselInd = 0

        def nextImage():
            st.session_state.carouselInd = (st.session_state.carouselInd + 1) % len(carouselImages)
        def prevImage():
            st.session_state.carouselInd = (st.session_state.carouselInd - 1) % len(carouselImages)

        with st.container(key="carouselContainer"):
            currentImg = carouselImages[st.session_state.carouselInd]
            img_text = charity.name
            st.markdown(f"""
                <div class="carousel-wrapper">
                    <img src="{currentImg}" class="carousel-img">
                    <div class="carousel-fade"></div>
                    <div class="carousel-overlay-text">{img_text}</div>
                </div>
            """, unsafe_allow_html=True)

            st.button("❮", key="prevBtn", on_click=prevImage, type="secondary")
            st.button("❯", key="nextBtn", on_click=nextImage, type="secondary")

        with st.container(key="charityDetailsCont"):
            main_cols = st.columns([5, 3])
            with main_cols[0]:
                with st.container(key="charityDetails"):
                    st.title("About")
                    st.text(charity.description)
            with main_cols[1]:
                st.link_button("Donate", charity.donationURL, use_container_width=True, key="charityButton1", type="tertiary")
                st.link_button("Website", charity.website, use_container_width=True, key="charityButton2", type="tertiary")

        dataManagement.charityVisited(charityId)
else:
    st.space("large")
    st.warning("Error - Page not found", icon="⚠️")