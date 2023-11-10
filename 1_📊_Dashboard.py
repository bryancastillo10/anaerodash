import streamlit as st
import streamlit_authenticator as stauth

from dataprocess.data_handling import *
from dataprocess.data_handling2 import *
from dataprocess.data_visualization import *
from utility.auxilliary import *
from utility.auth import user_auth_system
from lang.language import select_language

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
    ## Multi-Language Options
    lang_dict = select_language()

    ## Main Caption
    st.title(lang_dict["title"] + ":potable_water:")
    st.markdown(
        lang_dict["dashcaption"],
        unsafe_allow_html=True,
    )

    ## Sidebar
    with st.sidebar:
        st.title(f"Welcome {name}!")
        st.header("Let's Get Started!")
        uploaded_file = st.file_uploader(
            ":file_folder: Upload your raw data here", type=(["csv"])
        )
        authenticator.logout("Logout", "sidebar")
        whitespaces(2)
        st.image("utility/images/biogas_plant.png", width=200)

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
            lang_dict["tab1"],  # "Time Series"
            lang_dict["tab2"],  # "Reduction Rates"
            lang_dict["tab3"],  # "Summary Statistics"
            lang_dict["tab4"],  # "Other Parameters"
            lang_dict["tab5"],  # "Correlation"
        ]
    )

    with tabs[0]:
        st.markdown(f"<h3>{lang_dict['timeseries']}</h3>", unsafe_allow_html=True)
        left_column, right_column = st.columns((2, 2))
        with left_column:
            st.subheader(lang_dict["timevis1"])
            time_series(df)
        with right_column:
            st.subheader(lang_dict["timevis2"])
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
        st.markdown(Correlation_Caption, unsafe_allow_html=True)
        inf, acid, AD = st.columns(3)
        figures = plot_corr(df)

        for i, figure in enumerate(figures):
            with inf if i < 2 else AD:
                st.plotly_chart(figure)
