import streamlit as st
from utility.auxilliary import *

st.set_page_config(page_title="Guidelines", page_icon="📖", layout="wide")
with open("utility/style.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

st.title(":green[Some Guidelines]  to use the dashboard app :potable_water:")

with st.sidebar:
    whitespaces(5)
    st.image("utility/images/biogas_plant.png", width=200)

## HTML Struture ##
Guide = """
<div class="grid-container">
<div class="item1"> <p>
    Anaerobic digestion is the natural process in which microorganisms break down organic materials.  
    In this instance, “organic” means coming from or made of plants or animals.
    Anaerobic digestion happens in closed spaces where there is no air (or oxygen). The initials “AD” may refer to
    the process of anaerobic digestion or the built system where anaerobic digestion takes place, also known as a digester.
    </p>
    <p>Since this web app is focused on anaerobic digestion (AD) system. To optimize the use of this app, 
    the following columns are suggested to be included in your raw data:</p>
</div>
<div class="item 2">
<table id="guideline">
    <tr>
      <th>Parameter</th>
      <th>Column Name Format</th>
      <th>Value Format</th>
      <th>APP Capabilities</th>
    </tr>
    <tr>
      <td>Date (in mm/dd/yyyy format)</td>
      <td>Date</td>
      <td>Datetime </td>
      <td>Used for Time Series Plots, Summary Statistics by HRT</td>
    </tr>
    <tr>
      <td>Influent and Reactor Unit</td>
      <td>Unit</td>
      <td>Categorical variables for this APP should be 
      <span class="unit_highlight">Influent</span>,
      <span class="unit_highlight">Acid_Tank</span> and 
      <span class="unit_highlight">AD</span> </td>
      <td>Used for Time Series Plots, Summary Statistics by HRT</td>
    </tr>
    <tr>
    <tr>
      <td>pH</td>
      <td>pH</td>
      <td>Integer (Typically from 1 to 14)</td>
      <td>Can provide Time Series Plot, Correlation with other water quality parameters</td>
    </tr>
    <tr>
      <td>Temperature (in degrees C)</td>
      <td>Temp</td>
      <td>Integer (Typically between 30 to 60)</td>
      <td>Can provide Time Series Plot, Correlation with other water quality parameters</td>
    </tr>
    <tr>
        <td>Oxidation Reduction Potential (in mV)</td>
        <td>ORP</td>
        <td>Integer (Typically between 0 to -500 for AD system)</td>
        <td>Can provide Time Series Plot, Correlation with other water quality parameters</td>
    </tr>
    <tr>
        <td>Total Chemical Oxygen Demand (in mg/L)</td>
        <td>CODt</td>
        <td>Integer (Value depends on the wastewater/waste to be treated)</td>
        <td>Can provide Time Series Plot, Reduction Rates, Correlation with other water quality parameters</td>
      </tr>
      <tr>
        <td>Soluble Chemical Oxygen Demand (in mg/L)</td>
        <td>CODs</td>
        <td>Integer (Value depends on the wastewater/waste to be treated, should be lower than total COD)</td>
        <td>Can provide Time Series Plot, Reduction Rates, Correlation with other water quality parameters</td>
      </tr>
      <tr>
        <td>Total Kjeldahl Nitrogen (in mg/L)</td>
        <td>TKN</td>
        <td>Integer (Value depends on the wastewater/waste to be treated)</td>
        <td>Can provide Time Series Plot, Bar Plot by Overall Average, Used to calculate Organic Nitrogen, Correlation with other water quality parameters</td>
      </tr>
      <tr>
        <td>Ammonia (in mg/L)</td>
        <td>NH3</td>
        <td>Integer (Value depends on the wastewater/waste to be treated, should be lower than TKN)</td>
        <td>Can provide Time Series Plot, Bar Plot by Overall Average, Used to calculate Organic Nitrogen, Correlation with other water quality parameters</td>
      </tr>
      <tr>
        <td>Total Solids (in %)</td>
        <td>TS</td>
        <td>Float (Value depends on the wastewater/waste to be treated, between 0 to 100 )</td>
        <td>Can provide Time Series Plot, Reduction Rate, Used to calculate VS/TS Ratio, Correlation with other water quality parameters</td>
      </tr>
      <tr>
        <td>Volatile Solids (in %)</td>
        <td>VS</td>
        <td>Float (Value depends on the wastewater/waste to be treated, between 0 to 100, should be lower than TS )</td>
        <td>Can provide Time Series Plot, Reduction Rate, Used to calculate VS/TS Ratio, Correlation with other water quality parameters</td>
      </tr>
      <tr>
        <td>Raw Biogas Reading (in mL)</td>
        <td>Biogas</td>
        <td>Integer (Value depends on the wastewater/waste to be treated)</td>
        <td>Can provide Time Series Plot per Reactor Volume </td>
      </tr>
  </table>
</div> 
<div class="item3">
   <p>In this table, you'll find a summary of the required parameters and capabilities of the app. You can create your raw dataset,
   saved in a CSV file, following these data formats. This app is currently designed for a two-stage anaerobic digestion system, which 
   is the most common configuration. Developers are planning to enhance its compatibility to support one-stage and other configurations 
   in future updates.</p>
</div>
</div>
    """

## Streamlit Layout ##
st.subheader("A Brief Introduction about the APP")
st.markdown(Guide, unsafe_allow_html=True)
