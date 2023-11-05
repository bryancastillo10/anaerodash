import streamlit as st
import pandas as pd
import duckdb

#Grouping the Continous Variables and Date by Category depending on User Selection
def GroupByUnit(df, unit):
    unit_df = duckdb.sql(
        f"""
        SELECT "Date", "pH", "Temp", "ORP", "CODt", "CODs", "TKN", "NH3", "TS", "VS"
        FROM df
        WHERE "Unit" = '{unit}';   
    """
    ).df()

    return unit_df

#Calculating the Summary Statistics by Date Interval(HRT) selected by User
def hrt_interval(unit_df, hrt):
    unit_df["Date"] = pd.to_datetime(unit_df["Date"], format="%d/%m/%Y")
    min_date = unit_df["Date"].min()
    unit_df["Date Interval"] = (unit_df["Date"] - min_date).dt.days // hrt + 1
    unit_df["Date Interval"] = "Interval " + unit_df["Date Interval"].astype(str)

    agg_funcs = {
        "pH": ["mean", "std"],
        "Temp": ["mean", "std"],
        "ORP": ["mean", "std"],
        "CODt": ["mean", "std"],
        "CODs": ["mean", "std"],
        "TKN": ["mean", "std"],
        "NH3": ["mean", "std"],
        "TS": ["mean", "std"],
        "VS": ["mean", "std"],
    }

    stat_df = unit_df.groupby("Date Interval").agg(agg_funcs)
    stat_df.columns = [f"{param}_{stat}" for param, stat in stat_df.columns]
    stat_df.reset_index(drop=True)

    return stat_df

#Calculating the Spearman Correlation of the Continous Variables per Category
def correlation_operation(df):
    inf_df = df[df["Unit"] == "Influent"]
    acid_df = df[df["Unit"] == "Acid_Tank"]
    AD_df = df[df["Unit"] == "AD"]

    def calculate_correlations(dataframe):
        columns_to_correlate = ["pH", "CODt", "CODs", "TKN", "NH3", "TS", "VS"]
        correlation_matrix = dataframe[columns_to_correlate].corr()
        return correlation_matrix

    inf_calc = calculate_correlations(inf_df)
    acid_calc = calculate_correlations(acid_df)
    AD_calc = calculate_correlations(AD_df)
    return inf_calc, acid_calc, AD_calc