import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dataprocess.data_handling import *
from dataprocess.data_handling2 import *

color_scheme = ["#66c2a5", "#fc8d62", "#a4b3e1", "#e78ac3", "#a6d854"]


# Water Quality Time Series Line Plots
def time_series(df):
    st.subheader("Water Quality")
    parameters = cont_paramaters(df)
    parameter_query = st.selectbox("Select a parameter:", parameters.columns)
    fig = px.line(
        df,
        x="Date",
        y=parameter_query,
        color="Unit",
        markers=True,
        title=f"{parameter_query} over Time",
    )
    for i, unit in enumerate(df["Unit"].unique()):
        fig.for_each_trace(
            lambda trace: trace.update(line=dict(color=color_scheme[i])),
            selector=dict(name=unit),
        )
    fig.update_traces(
        textposition="top center",
        marker=dict(size=8),
        selector=dict(mode="markers+lines"),
    )
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="left", x=0)
    )
    fig.update_xaxes(type="category")
    st.plotly_chart(fig, use_container_width=True)


# Biogas Production Time Series Plot
def biogas_plot(df, volume):
    df2 = biogas_calc(df, volume)
    fig = px.line(
        df2,
        x="Date",
        y="Biogas_Per_Volume",
        markers="True",
        title="Raw Biogas Production per Reactor Volume",
        color_discrete_sequence=["#FFCC00"],
    )
    fig.update_traces(
        textposition="top center",
        marker=dict(size=8),
        selector=dict(mode="markers+lines"),
    )
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=-0.7, xanchor="left", x=0)
    )

    st.plotly_chart(fig, use_container_width=True)


# COD Reduction Rate Line Plot
def COD_red(df):
    st.subheader("COD Reduction Rates (in %)")
    df2 = COD_red_calc(df)
    fig = px.line(
        df2,
        x="Date",
        y=["CODt_Reduction", "CODs_Reduction"],
        markers=True,
        color_discrete_sequence=["#fc8d62", "#66c2a5"],
    )
    fig.update_layout(yaxis_title="Reduction Rate (%)")
    st.plotly_chart(fig, use_container_width=True)


# Solids Reduction Rate Line Plot
def solids_red(df):
    st.subheader("Solids Reduction Rates (in %)")
    df2 = solids_red_calc(df)
    fig = px.line(
        df2,
        x="Date",
        y=["TS_Reduction", "VS_Reduction"],
        markers=True,
        color_discrete_sequence=["#fc8d62", "#66c2a5"],
    )
    fig.update_layout(yaxis_title="Reduction Rate (%)")
    st.plotly_chart(fig, use_container_width=True)


# VS/TS Time Series Line Plot
def solids_ratio_series(df):
    st.subheader("VS/TS")
    df2 = solids_ratio(df)
    fig = px.line(
        df2,
        x="Date",
        y="Solids_Ratio",
        color="Unit",
        markers=True,
        color_discrete_sequence=["#fc8d62", "#66c2a5"],
    )
    for i, unit in enumerate(df["Unit"].unique()):
        fig.for_each_trace(
            lambda trace: trace.update(line=dict(color=color_scheme[i])),
            selector=dict(name=unit),
        )
    fig.update_layout(yaxis_title="VS/TS")
    st.plotly_chart(fig, use_container_width=True)


# Average Nitrogen Grouped Bar Plot
def Nitrogen(df):
    st.subheader("Average Nitrogen Concentration")
    df2 = OrganicN(df)
    fig = px.bar(
        df2,
        x="Unit",
        y=["AVG_TKN", "AVG_NH3", "AVG_OrgN"],
        color="variable",
        labels={
            "AVG_TKN": "Average TKN",
            "AVG_NH3": "Average NH3",
            "AVG_OrgN": "Average OrgN",
        },
    )
    fig.update_layout(barmode="group")
    for i, col in enumerate(df2.columns[1:]):
        fig.data[i].marker.color = color_scheme[i]
    fig.update_layout(yaxis_title="Concentration (mg N/L)")
    st.plotly_chart(fig, use_container_width=True)


# Correlation Heatmap
def plot_corr(df):
    inf, acid, AD = correlation_operation(df)
    figures = []
    dfs = [inf, acid, AD]
    titles = [
        "Correlation Matrix for Influent",
        "Correlation Matrix for Acid Tank",
        "Correlation Matrix for AD",
    ]
    for i, df in enumerate(dfs):
        fig = go.Figure(
            data=go.Heatmap(
                z=df.corr().values,
                x=df.columns,
                y=df.columns,
                colorscale="RdBu",
            )
        )
        fig.update_layout(
            title=titles[i],
            xaxis_title="Water Quality Parameters",
            yaxis_title="Water Quality Parameters",
        )
        figures.append(fig)
    return figures
