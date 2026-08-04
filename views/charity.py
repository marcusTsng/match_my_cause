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
        st.warning("Error - Charity not found", icon="⚠️")

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

    placeholder_images = [
        charity.image1URL,
        charity.image2URL
    ]
    
    if 'carousel_idx' not in st.session_state:
        st.session_state.carousel_idx = 0

    def next_image(): 
        st.session_state.carousel_idx = (st.session_state.carousel_idx + 1) % len(placeholder_images)
    def prev_image(): 
        st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % len(placeholder_images)

    # --- CAROUSEL SECTION ---
    with st.container(key="carousel_container"):
        # Carousel Image & Content
        current_img = placeholder_images[st.session_state.carousel_idx]
        img_text = charity.name
        st.markdown(f"""
            <div class="carousel-wrapper">
                <img src="{current_img}" class="carousel-img">
                <div class="carousel-fade"></div>
                <div class="carousel-overlay-text">{img_text}</div>
            </div>
        """, unsafe_allow_html=True)

        # Carousel Navigation Buttons
        st.button("❮", key="prevBtn", on_click=prev_image, type="secondary")
        st.button("❯", key="nextBtn", on_click=next_image, type="secondary")

    # --- MAIN DETAILS SECTION ---
    with st.container(key="charity_page_details_box"):
        main_cols = st.columns([5, 3])
        with main_cols[0]: # DESCRIPTION
            st.markdown(f'<h2 class="centeredTitle">About Us</h2>', unsafe_allow_html=True)
            description = "Error while accessing details. Organisation has likely not provided details for the charity."
            st.markdown(f'<p class="centeredDesc">{description}</p>', unsafe_allow_html=True)
        with main_cols[1]: # BUTTONS
            st.button("Donate", use_container_width=True, key="charity-button-1")
            st.button("Contact", use_container_width=True, key="charity-button-2")
            st.button("Register", use_container_width=True, key="charity-button-3")

    dataManagement.charityVisited(charityId)
else:
    st.warning("Error - Page not found", icon="⚠️")