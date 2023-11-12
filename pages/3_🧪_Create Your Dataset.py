import streamlit as st
import pandas as pd
import numpy as np

from dataprocess.data_handling import load_csv
from utility.auth import user_auth_system
from utility.auxilliary import whitespaces
from lang.language import select_language

st.set_page_config(page_title="Create your Dataset", page_icon="🧪", layout="wide")
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
    text = select_language(page_num=3)

    st.title(f":green[{text['title1']}] " + text['title2'] + ":potable_water:")

    with st.sidebar:
        whitespaces(2)
        st.image("utility/images/biogas_plant.png", width=200)
        whitespaces(1)
        authenticator.logout(text["logout"], "sidebar")

    st.markdown(f"""
    
    <p>{text['caption1']}</p>
    """,unsafe_allow_html=True)
    sample_df = pd.DataFrame(
        [
            {
                "Date": "01/10/2020",
                "Unit": "Influent",
                "pH": "5.6",
                "Temp": "",
                "ORP": "-100",
                "CODt": "20000",
                "CODs": "12000",
                "TKN": "2000",
                "NH3": "1500",
                "TS": "2.1",
                "VS": "1.5",
                "Biogas": "",
            },
            {
                "Date": "01/10/2020",
                "Unit": "Acid_Tank",
                "pH": "6.1",
                "Temp": "36",
                "ORP": "-100",
                "CODt": "20000",
                "CODs": "12000",
                "TKN": "3000",
                "NH3": "1800",
                "TS": "1.8",
                "VS": "1.0",
                "Biogas": "",
            },
            {
                "Date": "01/10/2020",
                "Unit": "AD",
                "pH": "7.4",
                "Temp": "37",
                "ORP": "-100",
                "CODt": "20000",
                "CODs": "12000",
                "TKN": "2000",
                "NH3": "1500",
                "TS": "1.4",
                "VS": "0.8",
                "Biogas": "450",
            },
        ]
    )
    ### Streamlit Layout
    left_column, right_column = st.columns((5,2))
    with left_column:
        new_df = st.data_editor(sample_df, num_rows="dynamic")    
        def convert_df(new_df):
            return new_df.to_csv(index=False).encode("utf-8")


        csv = convert_df(new_df)

        st.download_button(
            f"""{text['download']}""", csv, "raw_data.csv", "text/csv", key="download-csv"
            )
    with right_column:
        st.markdown(f"""
        <h2>{text['caption2']}</h2>
        <table id="legendformat">
        <tr>
        <td>{text['dt']}</td>
        <td>mm/dd/yyyy</td>
        </tr>
        <tr>
        <td>{text['reactor']}</td>
        <td>Influent; Acid_Tank; AD</td>
        </tr>
        <tr>
        <td>ORP</td>
        <td>{text['negint']}</td>
        </tr>
        <tr>
        <td>TS,VS</td>
        <td>{text['fl']}</td>
        </tr>
        <tr>
        <td>{text['others']}</td>
        <td>{text['int']}</td>
        </tr>
        </table>
        """,unsafe_allow_html=True)