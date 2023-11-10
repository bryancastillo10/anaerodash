import streamlit as st


def whitespaces(n):
    for _ in range(n):
        st.sidebar.markdown("<br>", unsafe_allow_html=True)


Reduction_Rates_Caption = """ 
<p>Measuring the reduction rates of CODt, CODs, TS, and VS in anaerobic digestion is critical for process control, 
optimization, and environmental compliance. It helps ensure the efficient conversion of organic matter into biogas and 
high-quality digestate while minimizing the environmental impact of organic waste disposal.</p>

"""
Calculating_HRT = """<h3>Summary Statistics by HRT</h3>
    <p>Monitoring Hydraulic Retention Time (HRT) in anaerobic digestion is crucial for assessing
    process stability and efficiency, as HRT influences microbial activity and contact time with organic material.
    Calculating the average HRT for specific date intervals is important for performance monitoring, process optimization,
    and troubleshooting. This approach allows operators to detect trends, identify operational issues, and make adjustments
    to maintain consistent and efficient biogas production, ensuring the system's reliability and performance.</p>"""

Other_Parameters = """<h3>Additional Parameters</h3><br>
    <p>These parameters were calculated based on the uploaded data. Nitrogen plays a crucial role in the anaerobic
    digestion process by supporting microbial growth and activity, maintaining the appropriate carbon-to-nitrogen ratio, 
    helping to control pH, and ensuring a balanced nutrient supply. Proper management of nitrogen and other nutrients is 
    essential for maximizing the biogas production and the overall efficiency of anaerobic digestion systems.</p>
    <p>Meanwhile, the VS/TS (Volatile Solids to Total Solids) ratio is a critical parameter in anaerobic digestion 
    (AD)as it quantifies the proportion of biodegradable organic matter in the feedstock. This ratio serves as an indicator
    of the potential energy and biogas production capacity, the efficiency of the AD process, and the need for process
    control and optimization. A higher VS/TS ratio signifies a feedstock with greater biogas potential, while changes
    in the ratio over time help in assessing process performance. It aids in feedstock selection and characterization,
    making it an essential tool for AD system planning and operation.</p>"""

Correlation_Caption = """
    <h3>Heatmaps representing Water Quality Correlations</h3>
    <p>Spearman correlation analysis is valuable in wastewater treatment, particularly in AD systems, 
    because it can handle non-linear, non-normally distributed, and potentially noisy data, 
    making it a useful tool for understanding the relationships between water quality parameters
    and optimizing the treatment process.</p>
"""

Create_Dataset = """<p>To have a more convenient approach in using the APP, you can create the table
using the table provided with the appropriate format. Please strictly follow the data format to be able
to use the Dashboard App. It should be noted that expression units on the guidelines section.</p>"""
