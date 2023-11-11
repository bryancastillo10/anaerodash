import streamlit as st
import streamlit_authenticator as stauth

from dataprocess.data_handling import *
from dataprocess.data_handling2 import *
from dataprocess.data_visualization import *

from lang.language import select_language
from utility.auth import user_auth_system
from utility.auxilliary import whitespaces

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
    text = select_language(page_num=1)
 
    ## Main Caption
    st.title(f":green[{text['title']}] " + text["title2"] + ":potable_water:")
    st.markdown(
        text["dashcaption"],
        unsafe_allow_html=True,
    )

    ## Sidebar
    with st.sidebar:
        st.title(f"{text['welcome']} {name}!")
        st.header(text["start"])
        uploaded_file = st.file_uploader(
            f":file_folder: {text['upload']}", type=(["csv"])
        )
        authenticator.logout(text["logout"], "sidebar")
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

    with st.expander(text['preview']):
        df = load_csv(uploaded_file)
        st.dataframe(df)

    ######### STREAMLIT LAYOUT #########
    tabs = st.tabs(
        [
            text["tab1"],  # "Time Series"
            text["tab2"],  # "Reduction Rates"
            text["tab3"],  # "Summary Statistics"
            text["tab4"],  # "Other Parameters"
            text["tab5"],  # "Correlation"
        ]
    )

    with tabs[0]:
        st.markdown(f"<h3>{text['timeseries']}</h3>", unsafe_allow_html=True)
        left_column, right_column = st.columns((2, 2))
        with left_column:
            st.subheader(text["timevis1"])
            time_series(df)
        with right_column:
            st.subheader(text["timevis2"])
            volume = st.radio(
                "Please choose the reactor volume (in mL)",
                [6000, 10000, 12000],
                horizontal=True,
            )
            biogas_plot(df, volume)

    with tabs[1]:
        st.markdown(f"<h3>{text['reductionrate']}</h3>", unsafe_allow_html=True)
        st.markdown(text["redcaption"])
        left_column, right_column = st.columns((2, 2))
        with left_column:
            st.subheader(text["codreduction"])
            COD_red(df)
        with right_column:
            st.subheader(text["solidreduction"])
            solids_red(df)

    with tabs[2]:
        st.markdown(f"<h3>{text['stat_title']}</h3>", unsafe_allow_html=True)
        st.markdown(text['statcaption'])
        units_choices = ["Influent", "Acid_Tank", "AD"]
        unit = st.selectbox(text['unitselect'], units_choices)

        hrt = st.slider(text['hrtselect'], 0, 30, 20, step=5)

        if st.button(text['showsummary']):
            unit_df = GroupByUnit(df, unit)
            hrt_summary = hrt_interval(unit_df, hrt)
            st.dataframe(hrt_summary, use_container_width=True)

    with tabs[3]:
        st.markdown(f"<h3>{text['otherparamcap']}</h3>", unsafe_allow_html=True)
        st.markdown(text['otherparam'])
        st.markdown(text['otherparam2'])
        left_column, right_column = st.columns((2, 2))
        with left_column:
            st.subheader(text['nitrogen'])
            Nitrogen(df)
        with right_column:
            solids_ratio_series(df)

    with tabs[4]:
        st.markdown(f"<h3>{text['corrtitle']}</h3>", unsafe_allow_html=True)
        st.markdown(text['corrcaption'])
        figures = plot_corr(df)
        left_column, right_column = st.columns((4,3))
        with left_column:
            st.subheader(text['corrinf'])
            figures[0]

        with right_column:
            st.subheader(text['corracid'])
            figures[1]    

        left, middle, right = st.columns((2, 5, 2))
        with middle:
            st.subheader(text['corrAD'])
            figures[2]
