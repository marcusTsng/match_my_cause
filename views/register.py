import streamlit as st

with st.container(key="registerPage"):
    with st.container(key="registerTitleContainer"):
        st.markdown('<h2 class="registerTitle">Register your own charity</h2>', unsafe_allow_html=True)
        st.markdown('<h2 class="registerTitleSmall">Register</h2>', unsafe_allow_html=True)

    with st.container(key="formContainer"):
        with st.form(key="registerCharity", clear_on_submit=True, enter_to_submit=False):
            formColumns = st.columns(2)
            with formColumns[0]:
                with st.container(key="formColumn1"):
                    newName = st.text_input("Charity Name", placeholder="Tell us your charity's name!")
                    newCategory = st.pills("Category",
                                           ["Animals", "Environment", "Education", "Poverty", "Healthcare", "Culture", "Rights", "Other"],
                                           required=True)

            with formColumns[1]:
                test2 = st.text_input("Tags")

            submitted = st.form_submit_button("Submit")
