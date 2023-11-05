import streamlit as st
import pandas as pd
import numpy as np

from utility.auxilliary import *
from dataprocess.data_handling import load_csv

st.set_page_config(page_title="Create your Dataset", page_icon="🧪", layout="wide")
with open("utility/style.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

st.title(":green[AnaeroDash APP] Generate your Raw Dataset Here :potable_water:")

with st.sidebar:
    whitespaces(5)
    st.image("utility/images/biogas_plant.png", width=200)

st.markdown(Create_Dataset,unsafe_allow_html=True)
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

new_df = st.data_editor(sample_df, num_rows="dynamic")


def convert_df(new_df):
    return new_df.to_csv(index=False).encode("utf-8")


csv = convert_df(new_df)

st.download_button(
    "Download your Raw Data", csv, "file.csv", "text/csv", key="download-csv"
)
