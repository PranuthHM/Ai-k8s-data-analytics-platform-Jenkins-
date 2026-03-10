import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import subprocess
# from streamlit_autorefresh import st_autorefresh
import time




# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(page_title="Colorado Motor Vehicle Sales Dashboard", layout="wide")




# ======================================================
# FUTURISTIC CYBERPUNK DESIGN
# ======================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
}

/* Animated Gradient Background */

.stApp {
background: linear-gradient(270deg,#0f0c29,#302b63,#24243e,#0f0c29);
background-size: 800% 800%;
animation: gradientBG 20s ease infinite;
}

@keyframes gradientBG {
0%{background-position:0% 50%}
50%{background-position:100% 50%}
100%{background-position:0% 50%}
}

/* Glass dashboard */

.block-container {
background: rgba(0,0,0,0.35);
backdrop-filter: blur(20px);
border-radius: 20px;
padding: 2rem;
box-shadow: 0 0 30px rgba(0,255,255,0.2);
}

/* Sidebar */

[data-testid="stSidebar"]{
background: linear-gradient(180deg,#0f2027,#203a43,#2c5364);
border-right:1px solid cyan;
}

/* Metric cards */

[data-testid="metric-container"]{
background: rgba(0,0,0,0.5);
border-radius:20px;
border:1px solid cyan;
padding:20px;
box-shadow:0 0 20px rgba(0,255,255,0.4);
transition:0.4s;
}

[data-testid="metric-container"]:hover{
transform:translateY(-8px) scale(1.05);
box-shadow:0 0 40px cyan;
}

/* Metric number */

[data-testid="metric-container"] div{
font-size:35px;
font-weight:bold;
color:#00ffff;
text-shadow:0 0 10px cyan;
}

/* Titles */

h1,h2,h3{
font-family:'Orbitron', sans-serif;
color:#00ffff;
text-shadow:0 0 10px cyan;
}

/* Buttons */

.stButton>button{
background:linear-gradient(45deg,#00ffff,#ff00ff);
border:none;
color:black;
border-radius:15px;
padding:10px 25px;
font-weight:bold;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.1);
box-shadow:0 0 20px #00ffff;
}

/* Tables */

[data-testid="stDataFrame"]{
background:rgba(0,0,0,0.4);
border:1px solid cyan;
border-radius:15px;
}

/* Chart glow */

canvas{
filter: drop-shadow(0px 0px 10px cyan);
}

/* Particle background */

#particles-js{
position:fixed;
width:100%;
height:100%;
top:0;
left:0;
z-index:-1;
}
/* SIDEBAR MAIN */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0f2027,#203a43,#2c5364);
    border-right: 1px solid cyan;
}

/* RADIO BUTTON CONTAINER */

div[role="radiogroup"] > label {
    background: rgba(0,0,0,0.35);
    padding: 12px 16px;
    margin-bottom: 8px;
    border-radius: 12px;
    border: 1px solid rgba(0,255,255,0.2);
    transition: all 0.35s ease;
    cursor: pointer;
    color: #ffffff;
}

/* HOVER ANIMATION */

div[role="radiogroup"] > label:hover {

    transform: translateX(8px) scale(1.03);

    background: linear-gradient(90deg,#00ffff33,#ff00ff33);

    border: 1px solid cyan;

    box-shadow: 0 0 12px cyan;

}

/* ACTIVE SELECTED */

div[role="radiogroup"] > label[data-selected="true"] {

    background: linear-gradient(90deg,#00ffff,#ff00ff);

    color: black;

    font-weight: bold;

    transform: scale(1.05);

    box-shadow: 0 0 15px #00ffff;

}

/* ICON ANIMATION */

div[role="radiogroup"] > label:hover span {

    animation: glowText 1s infinite alternate;

}

@keyframes glowText {

    from { text-shadow:0 0 5px cyan; }

    to { text-shadow:0 0 15px cyan; }

}

/* SIDEBAR HEADER */

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {

    color:#00ffff;

    text-shadow:0 0 10px cyan;

}
</style>

<div id="particles-js"></div>

<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>

<script>
particlesJS("particles-js",{
"particles":{
"number":{"value":80},
"color":{"value":"#00ffff"},
"shape":{"type":"circle"},
"opacity":{"value":0.6},
"size":{"value":3},
"line_linked":{
"enable":true,
"distance":150,
"color":"#00ffff",
"opacity":0.4,
"width":1
},
"move":{
"enable":true,
"speed":3
}
},
"interactivity":{
"events":{
"onhover":{"enable":true,"mode":"repulse"},
"onclick":{"enable":true,"mode":"push"}
}
}
});
</script>
""", unsafe_allow_html=True)



st.title("🚗 Colorado Motor Vehicle Sales Analysis & Forecasting")




# ======================================================
# Kubernetes Metrics Function
# ======================================================

def get_pod_metrics():

    try:

        result = subprocess.run(
            ["kubectl", "top", "pods", "--no-headers"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0 or result.stdout.strip() == "":
            return pd.DataFrame()

        lines = result.stdout.strip().split("\n")

        data = []

        for line in lines:

            parts = line.split()

            if len(parts) < 3:
                continue

            pod = parts[0]

            cpu = parts[1].replace("m", "")
            memory = parts[2].replace("Mi", "")

            data.append({
                "pod": pod,
                "cpu": int(cpu),
                "memory": int(memory)
            })

        return pd.DataFrame(data)

    except Exception as e:

        print("Error getting metrics:", e)

        return pd.DataFrame()




# Load Data
df = pd.read_csv("colorado_motor_vehicle_sales.csv")




# Sidebar
st.sidebar.header("📌 Navigation")
option = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "EDA",
        "County Analysis",
        "Forecasting",
        "Project Details",
        "AI Monitoring"
    ]
)




# ======================================================
# OVERVIEW
# ======================================================
if option == "Overview":

    st.header("📊 Overview Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sales", f"${df.sales.sum():,.0f}")
    col2.metric("Average Sales", f"${df.sales.mean():,.0f}")
    col3.metric("Total Records", len(df))

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head(20))

    st.subheader("📈 Sales Trend Over Years")
    yearly = df.groupby("year")["sales"].sum()

    fig, ax = plt.subplots(figsize=(10,4))
    yearly.plot(marker='o', ax=ax)
    ax.set_ylabel("Total Sales")
    st.pyplot(fig)

    st.subheader("📊 Sales by Quarter")

    fig2, ax2 = plt.subplots()
    sns.barplot(x="quarter", y="sales", data=df, ax=ax2)
    st.pyplot(fig2)
    
    st.success("📊 Overview Dashboard performed successfully")







# ======================================================
# EDA
# ======================================================
elif option == "EDA":

    st.header("📊 Exploratory Data Analysis")

    st.subheader("Quarter-wise Sales Distribution")

    fig, ax = plt.subplots()
    sns.boxplot(x=df['quarter'], y=df['sales'], ax=ax)
    st.pyplot(fig)

    st.subheader("County-wise Total Sales")

    county_total = df.groupby("county")["sales"].sum().sort_values(ascending=False)

    fig2, ax2 = plt.subplots(figsize=(10,4))
    county_total.head(10).plot(kind='bar', ax=ax2)
    st.pyplot(fig2)

    st.subheader("Correlation Heatmap")

    pivot = df.pivot_table(values='sales', index='year', columns='county')

    fig3, ax3 = plt.subplots(figsize=(8,6))
    sns.heatmap(pivot.corr(), cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)
    
    
    st.success("📊 Exploratory Data Analysis performed successfully")




# ======================================================
# COUNTY ANALYSIS
# ======================================================
elif option == "County Analysis":

    st.header("🏙 County-Level Analysis")

    tab1, tab2 = st.tabs(["📊 Year & Quarter Filter", "📈 County Trend"])

    with tab1:

        year = st.selectbox("Select Year", sorted(df.year.unique()))
        quarter = st.selectbox("Select Quarter", [1,2,3,4])

        temp = df[(df.year==year) & (df.quarter==quarter)]

        county_sales = temp.groupby('county')['sales'].sum()

        fig, ax = plt.subplots(figsize=(12,4))
        county_sales.plot(kind='bar', ax=ax)
        st.pyplot(fig)

    with tab2:

        selected_county = st.selectbox("Select County", df['county'].unique())

        county_ts = df[df['county']==selected_county]
        county_ts = county_ts.groupby("year")["sales"].sum()

        fig2, ax2 = plt.subplots()
        county_ts.plot(marker='o', ax=ax2)
        st.pyplot(fig2)
        
    st.success("Country Analysis performed successfully")






# ======================================================
# FORECASTING
# ======================================================
elif option == "Forecasting":

    st.header("🔮 Sales Forecasting")

    df['month'] = df['quarter'].map({1:1,2:4,3:7,4:10})
    df['date'] = pd.to_datetime(df[['year','month']].assign(day=1))

    ts = df.groupby('date')['sales'].sum()

    ts.index = pd.PeriodIndex(ts.index, freq='Q').to_timestamp()

    fig, ax = plt.subplots()
    ts.plot(ax=ax)
    st.pyplot(fig)

    model = ARIMA(ts, order=(1,1,1))
    fit = model.fit()
    forecast = fit.forecast(steps=8)

    fig2, ax2 = plt.subplots()
    ts.plot(label="Actual", ax=ax2)
    forecast.plot(label="Forecast", ax=ax2)
    ax2.legend()
    st.pyplot(fig2)
    
    st.success("Sales Forecasting performed successfully")








# ======================================================
# PROJECT DETAILS
# ======================================================
elif option == "Project Details":
    st.header("📌 Project Information")

    st.markdown("""
    ### 🚗 Colorado Motor Vehicle Sales Analysis & Forecasting
    
    **Developed By:** Pranuth Manjunath  
    **Domain:** MLOps  
    **Tools Used:** Python, Pandas, Seaborn, ARIMA, Streamlit, Docker, Kubernetes  
    """)

    st.markdown("### 📂 Download Files")

    # Download CSV
    with open("colorado_motor_vehicle_sales.csv", "rb") as file:
        st.download_button(
            label="Download Dataset (CSV)",
            data=file,
            file_name="colorado_motor_vehicle_sales.csv"
        )

    # Download Notebook
    st.markdown("### 📓 Download Jupyter File")
    try:
        with open("main.ipynb", "rb") as f:
            st.download_button(
                label="📓 Download Jupyter Notebook (main.ipynb)",
                data=f,
                file_name="main.ipynb",
                mime="application/octet-stream"
        )
    except:
        st.info("Notebook file not found. Add project_notebook.ipynb in folder.")

    st.markdown("### 🔗 GitHub Repository")
    if st.button("🔗 Visit GitHub Project"):
        st.write("Opening GitHub...")
        st.markdown("https://github.com/PranuthHM/ai-k8s-data-analytics-platform")


    st.success("Thank you for reviewing this project!")







# ======================================================
# AI MONITORING
# ======================================================


elif option == "AI Monitoring":

    st.header("🤖 AI Kubernetes Resource Monitoring")

    st.markdown("""
    This section monitors Kubernetes pod resource utilization in real time.
    CPU and Memory metrics are collected using `kubectl top pods`.
    The system simulates AI-based prediction for future resource usage.
    """)

    df_metrics = get_pod_metrics()

    if not df_metrics.empty:

        # initialize history
        if "cpu_history" not in st.session_state:
            st.session_state.cpu_history = []

        cpu_total = df_metrics["cpu"].sum()

        st.session_state.cpu_history.append(cpu_total)

        if len(st.session_state.cpu_history) > 30:
            st.session_state.cpu_history.pop(0)

        st.subheader("📦 Active Kubernetes Pods")
        st.dataframe(df_metrics)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📈 CPU Usage per Pod")
            st.line_chart(df_metrics.set_index("pod")["cpu"])

        with col2:
            st.subheader("💾 Memory Usage per Pod")
            st.bar_chart(df_metrics.set_index("pod")["memory"])

        st.subheader("⚡ Real-Time Cluster CPU Usage")
        st.line_chart(st.session_state.cpu_history)

        df_metrics["predicted_cpu"] = df_metrics["cpu"] * 1.15

        st.subheader("🤖 AI Predicted CPU Trend")
        st.line_chart(df_metrics.set_index("pod")[["cpu","predicted_cpu"]])

        
        st.info("""
        🔹 **Kubernetes Pod Explanation**

        Each Pod represents a running instance of the containerized analytics application.
        The Deployment controller ensures that the defined number of replicas remain active.

        If a pod crashes or is deleted, Kubernetes automatically creates a new pod.
        This feature is called **Self-Healing Infrastructure**.
        """)
        
        st.metric("Active Pods", len(df_metrics))

        st.success("Real-time Kubernetes Monitoring Active")

    else:
        st.warning("Metrics not available yet. Waiting for Kubernetes metrics...")

    time.sleep(3)
    st.rerun()