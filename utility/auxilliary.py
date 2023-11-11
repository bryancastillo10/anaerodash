import streamlit as st

def whitespaces(n):
    for _ in range(n):
        st.sidebar.markdown("<br>", unsafe_allow_html=True)

Create_Dataset = """<p>To have a more convenient approach in using the APP, you can create the table
using the table provided with the appropriate format. Please strictly follow the data format to be able
to use the Dashboard App. It should be noted that expression units on the guidelines section.</p>"""
