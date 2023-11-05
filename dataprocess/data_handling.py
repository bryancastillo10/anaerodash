import streamlit as st
import pandas as pd
import duckdb
import time


# Uploading the raw data
@st.cache_data
def load_csv(file):
    df = pd.read_csv(file)
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y").dt.date
    df = df.fillna(0)
    return df


# Filtering the dataframe with the continuous variables
def cont_paramaters(df):
    parameters = duckdb.sql(
        f"""WITH parameters AS (
        SELECT pH, Temp, ORP, CODt, CODs, TKN, NH3,TS,VS
        FROM df
    )
    SELECT * FROM parameters
    """
    ).df()
    return parameters


def biogas_calc(df, volume):
    parameters = duckdb.sql(
        f"""
        SELECT Date, Biogas,
        Biogas/{volume} AS Biogas_Per_Volume
        FROM df
        WHERE Unit = 'AD'
        """
    ).df()
    return parameters


# Calculating the COD reduction
def COD_red_calc(df):
    rate = duckdb.sql(
        f"""
    SELECT Date, CODt_Reduction, CODs_Reduction
    FROM (
        SELECT DATE_TRUNC('day', Date) AS Date,
            (MAX(CASE WHEN Unit = 'Influent' THEN CODt END) - MAX(CASE WHEN Unit = 'AD' THEN CODt END))
            / MAX(CASE WHEN Unit = 'Influent' THEN CODt END) * 100 AS CODt_Reduction,
            (MAX(CASE WHEN Unit = 'Influent' THEN CODs END) - MAX(CASE WHEN Unit = 'AD' THEN CODs END))
            / MAX(CASE WHEN Unit = 'Influent' THEN CODs END) * 100 AS CODs_Reduction
        FROM df
        GROUP BY Date
    )
    ORDER BY Date
    """
    ).df()
    return rate


# Calculating the Solids reduction
def solids_red_calc(df):
    rate = duckdb.sql(
        f"""
    SELECT Date, TS_Reduction, VS_Reduction
    FROM (
        SELECT DATE_TRUNC('day', Date) AS Date,
            (MAX(CASE WHEN Unit = 'Influent' THEN TS END) - MAX(CASE WHEN Unit = 'AD' THEN TS END))
            / MAX(CASE WHEN Unit = 'Influent' THEN TS END) * 100 AS TS_Reduction,
            (MAX(CASE WHEN Unit = 'Influent' THEN VS END) - MAX(CASE WHEN Unit = 'AD' THEN VS END))
            / MAX(CASE WHEN Unit = 'Influent' THEN VS END) * 100 AS VS_Reduction
        FROM df
        GROUP BY Date
    )
    ORDER BY Date
    """
    ).df()
    return rate


# Calculating the VS/TS ratio
def solids_ratio(df):
    ratio = duckdb.sql(
        f"""      SELECT Date, Unit, Solids_Ratio
    FROM (
        SELECT DATE_TRUNC('day', Date) AS Date, Unit,
        VS/TS AS Solids_Ratio
        FROM df
    )   """
    ).df()
    return ratio


# Calculating the Organic Nitrogen and Sorting by Categorical Variable (Influent,Acid_Tank, and AD)
def OrganicN(df):
    OrgN = duckdb.sql(
        f"""SELECT Unit,
            AVG(TKN) AS AVG_TKN, 
            AVG(NH3) AS AVG_NH3,
            AVG(TKN - NH3) AS AVG_OrgN,
           FROM df
           WHERE Unit IN ('Influent', 'Acid_Tank', 'AD')
           GROUP BY Unit
            ORDER BY
            CASE
                   WHEN Unit = 'Influent' THEN 1
                   WHEN Unit = 'Acid_Tank' THEN 2
                   WHEN Unit = 'AD' THEN 3
            END
        """
    ).df()
    return OrgN
