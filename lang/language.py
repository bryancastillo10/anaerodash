import streamlit as st
import pandas as pd


def change_page1_language(locale, selected_lang):
    df = pd.read_csv("lang/text_bundle_dashboard.csv")
    df = df.query(f"locale == '{locale}'")
    lang_dict = {
        df.key.to_list()[i]: df.value.to_list()[i] for i in range(len(df.key.to_list()))
    }
    return lang_dict


def select_language():
    lang_options = {"English (US)": "en_us", "中文傳統": "zh_tw"}
    selected_lang = st.sidebar.selectbox(
        "APP Language", options=list(lang_options.keys())
    )
    lang_dict = change_page1_language(lang_options[selected_lang], selected_lang)
    return lang_dict
