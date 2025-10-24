
import streamlit as st

# Streamlit App Configuration
st.set_page_config(layout="centered", page_title="CrapGPT")

st.title("a worse version of chatgpt")


# Sidebar for page navigation
page = st.sidebar.radio("Navigate", ["Chat", "About Us"])

#Button to reset the app and clear session

if st.sidebar.button("Clear memory + re-run"):
    st.session_state.clear()
    st.rerun()