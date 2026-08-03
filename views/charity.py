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
    if not charity: st.warning("Error - Charity not found", icon="⚠️")

    st.set_page_config(page_title=charity.name)

    # charity : dataManagement.Charity = dataManagement.loadCharities()[charityId - 1]

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
        "https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg",
        "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?q=80&w=1000"
    ]
    
    if 'carousel_idx' not in st.session_state:
        st.session_state.carousel_idx = 0

    def next_image(): st.session_state.carousel_idx = (st.session_state.carousel_idx + 1) % len(placeholder_images)
    def prev_image(): st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % len(placeholder_images)


    carousel_cols = st.columns([1, 8, 1], vertical_alignment="center")
    
    with carousel_cols[0]:
        st.button("❮", key="prevBtn", on_click=prev_image, type="secondary")
        
    with carousel_cols[1]:
        current_img = placeholder_images[st.session_state.carousel_idx]
        img_text = "placeholder text here blah blah blah blah blah"
        st.markdown(f"""
            <div class="carousel-wrapper">
                <img src="{current_img}" class="carousel-img">
                <div class="carousel-fade"></div>
                <div class="carousel-overlay-text">{img_text}</div>
            </div>
        """, unsafe_allow_html=True)
        
    with carousel_cols[2]:
        st.button("❯", key="nextBtn", on_click=next_image, type="secondary")


    st.markdown(f'<h2 class="centeredTitle">{charity.name}</h2>', unsafe_allow_html=True)
    
    description = "Error while accessing details. Organisation has likely not provided details for the charity."
    st.markdown(f'<p class="centeredDesc">{description}</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # End app-card-layout


    with st.container(key="bottomNavBar"):        
        st.markdown('<div class="bottom-button-strip">', unsafe_allow_html=True)
        nav_cols = st.columns(3)
        with nav_cols[0]:
            st.button("Placeholder 1", use_container_width=True, key="p1")
        with nav_cols[1]:
            st.button("Placeholder 2", use_container_width=True, key="p2")
        with nav_cols[2]:
            st.button("Placeholder 3", use_container_width=True, key="p3")
        st.markdown('</div>', unsafe_allow_html=True)


    dataManagement.charityVisited(charityId)
else:
    st.warning("Error - Page not found", icon="⚠️")