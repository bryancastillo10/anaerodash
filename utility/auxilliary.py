import streamlit as st

def whitespaces(n):
    for _ in range(n):
        st.sidebar.markdown("<br>", unsafe_allow_html=True)


