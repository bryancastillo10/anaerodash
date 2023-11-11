import streamlit as st
from utility.auxilliary import whitespaces, Guide
from utility.auth import user_auth_system
from lang.language import select_language

st.set_page_config(page_title="Guidelines", page_icon="📖", layout="wide")
with open("utility/style.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

##User Authentication System ###
name, authentication_status, username, authenticator = user_auth_system()
if authentication_status == False:
    st.error("Username/Password is incorrect 😣")

if authentication_status == None:
    st.info(
        "Welcome to the AnaeroDash APP: An Application dedicated for Anaerobic Digestion Treatment Plant Evaluation.\
        Please login with appropriate username and password to get started.",
        icon="🌐",
    )
    st.markdown("Prototype_v_1.0 made by Bryan")

if authentication_status:
  ## Multi-Language Options
  text = select_language(page_num=2)

  st.title(f":green[{text['guidetitle']}] " + text['guidetitle2'] + ":potable_water:")

  with st.sidebar:
    st.title(text['welcome'])

    whitespaces(5)
    st.image("utility/images/biogas_plant.png", width=200)

  ## Streamlit Layout ##
  st.subheader(text['app_intro'])
  st.markdown(Guide, unsafe_allow_html=True)
