import streamlit as st
import streamlit_authenticator as stauth

from dataprocess.data_handling import *
from dataprocess.data_handling2 import *
from dataprocess.data_visualization import *
from utility.auxilliary import *
from utility.auth import user_auth_system

##### PAGE SETUP #####
st.set_page_config(page_title="AnaeroDash APP", page_icon=":clipboard:", layout="wide")

## Allowing CSS for webpage design
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
    st.title(":green[AnaeroDash APP]  Dedicated for AD System Evaluation :potable_water:")
    st.markdown(
        Dashboard_Caption,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.title(f"Welcome {name}!")
        st.header("Let's Get Started!")
        uploaded_file = st.file_uploader(
            ":file_folder: Upload your raw data here", type=(["csv"])
        )
        authenticator.logout("Logout", "sidebar")
        whitespaces(2)
        st.image("utility/images/biogas_plant.png", width=200)

    ## Multi-Language Options
    target_language = st.sidebar.selectbox("APP Language", ["English (US)","中文（傳統）"])


    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()

        if file_extension == "csv":
            load_csv(uploaded_file)

    else:
        st.info(
            "Welcome to the AnaeroDash App. Please upload a CSV file type to get started.",
            icon="ℹ️",
        )
        st.stop()

    with st.expander(" Uploaded Data Preview"):
        df = load_csv(uploaded_file)
        st.dataframe(df)

    ######### STREAMLIT LAYOUT #########
    tabs = st.tabs(
        [
            "Time Series",
            "Reduction Rates",
            "Summary Statistics",
            "Other Parameters",
            "Correlation",
        ]
    )

    with tabs[0]:
        st.markdown("<h3>Time Series Plots</h3>", unsafe_allow_html=True)
        left_column, right_column = st.columns((2, 2))
        with left_column:
            time_series(df)
        with right_column:
            st.subheader("AD Biogas Production")
            volume = st.radio(
                "Please choose the reactor volume (in mL)",
                [6000, 10000, 12000],
                horizontal=True,
            )
            biogas_plot(df, volume)

    with tabs[1]:
        st.markdown(Reduction_Rates_Caption, unsafe_allow_html=True)
        left_column, right_column = st.columns((2, 2))
        with left_column:
            COD_red(df)
        with right_column:
            solids_red(df)

    with tabs[2]:
        st.markdown(
            Calculating_HRT,
            unsafe_allow_html=True,
        )
        units_choices = ["Influent", "Acid_Tank", "AD"]
        unit = st.selectbox("Please choose a unit", units_choices)

        hrt = st.slider("Select the HRT(days)", 0, 30, 20, step=5)

        if st.button("Show the Summary"):
            unit_df = GroupByUnit(df, unit)
            hrt_summary = hrt_interval(unit_df, hrt)
            st.dataframe(hrt_summary, use_container_width=True)

    with tabs[3]:
        st.markdown(
            Other_Parameters,
            unsafe_allow_html=True,
        )
        left_column, right_column = st.columns((2, 2))
        with left_column:
            Nitrogen(df)
        with right_column:
            solids_ratio_series(df)

    with tabs[4]:
        st.markdown(
            Correlation_Caption, unsafe_allow_html=True
        )
        inf, acid, AD = st.columns(3)
        figures = plot_corr(df)

        for i, figure in enumerate(figures):
            with inf if i < 2 else AD:
                st.plotly_chart(figure)
