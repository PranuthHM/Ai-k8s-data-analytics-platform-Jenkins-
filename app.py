import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(page_title="Colorado Motor Vehicle Sales Dashboard", layout="wide")

st.title("🚗 Colorado Motor Vehicle Sales Analysis & Forecasting")

# Load Data
df = pd.read_csv("colorado_motor_vehicle_sales.csv")

# Sidebar Navigation
st.sidebar.header("📌 Navigation")
option = st.sidebar.radio(
    "Select Section",
    ["Overview", "EDA", "County Analysis", "Forecasting", "Project Details"]
)

# ======================================================
# 1️⃣ OVERVIEW SECTION
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


# ======================================================
# 2️⃣ EDA SECTION
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
    ax2.set_title("Top 10 Counties by Sales")
    st.pyplot(fig2)

    st.subheader("Correlation Heatmap")
    pivot = df.pivot_table(values='sales', index='year', columns='county')
    fig3, ax3 = plt.subplots(figsize=(8,6))
    sns.heatmap(pivot.corr(), cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)
    st.success("EDA Operations performed successfully!")



# ======================================================
# 3️⃣ COUNTY ANALYSIS (WITH SUBSECTIONS)
# ======================================================
elif option == "County Analysis":
    st.header("🏙 County-Level Analysis")

    tab1, tab2 = st.tabs(["📊 Year & Quarter Filter", "📈 County Trend Over Time"])

    # TAB 1
    with tab1:
        year = st.selectbox("Select Year", sorted(df.year.unique()))
        quarter = st.selectbox("Select Quarter", [1,2,3,4])

        temp = df[(df.year==year) & (df.quarter==quarter)]
        county_sales = temp.groupby('county')['sales'].sum().sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(12,4))
        county_sales.plot(kind='bar', ax=ax)
        ax.set_title(f"Sales by County - {year} Q{quarter}")
        st.pyplot(fig)
        
        st.success("Country Analysis 📊 Year & Quarter Filter generated successfully!")

    # TAB 2
    with tab2:
        selected_county = st.selectbox("Select County", df['county'].unique())

        county_ts = df[df['county']==selected_county]
        county_ts = county_ts.groupby("year")["sales"].sum()

        fig2, ax2 = plt.subplots()
        county_ts.plot(marker='o', ax=ax2)
        ax2.set_title(f"{selected_county} Sales Trend")
        st.pyplot(fig2)
        
        st.success("Country Analysis's 📈 County Trend Over Time Generated successfully!")



# ======================================================
# 4️⃣ FORECASTING SECTION
# ======================================================
elif option == "Forecasting":
    st.header("🔮 Sales Forecasting")

    try:
        # Create proper datetime index
        df['month'] = df['quarter'].map({1:1,2:4,3:7,4:10})
        df['date'] = pd.to_datetime(df[['year','month']].assign(day=1))

        ts = df.groupby('date')['sales'].sum()

        # IMPORTANT: Do NOT use asfreq blindly
        ts.index = pd.PeriodIndex(ts.index, freq='Q').to_timestamp()

        st.subheader("📈 Historical Sales Trend")
        fig, ax = plt.subplots()
        ts.plot(ax=ax)
        st.pyplot(fig)

        st.subheader("📊 Moving Average (4 Quarters)")
        moving_avg = ts.rolling(window=4).mean()

        fig2, ax2 = plt.subplots()
        ts.plot(label="Actual", ax=ax2)
        moving_avg.plot(label="Moving Avg", ax=ax2)
        ax2.legend()
        st.pyplot(fig2)

        st.subheader("📉 ARIMA Forecast (Next 8 Quarters)")

        model = ARIMA(ts, order=(1,1,1))
        fit = model.fit()
        forecast = fit.forecast(steps=8)

        fig3, ax3 = plt.subplots()
        ts.plot(label="Actual", ax=ax3)
        forecast.plot(label="Forecast", ax=ax3)
        ax3.legend()
        st.pyplot(fig3)

        st.success("Forecast generated successfully!")

    except Exception as e:
        st.error(f"Forecasting failed: {e}")


# ======================================================
# 5️⃣ PROJECT DETAILS SECTION
# ======================================================
elif option == "Project Details":
    st.header("📌 Project Information")

    st.markdown("""
    ### 🚗 Colorado Motor Vehicle Sales Analysis & Forecasting
    
    **Developed By:** Pranuth Manjunath  
    **Domain:** Finance Analytics / Data Science  
    **Tools Used:** Python, Pandas, Seaborn, ARIMA, Streamlit  
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

import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st


st.subheader("AI CPU Usage Prediction")


# Step 1: Get CPU usage from Kubernetes
def get_cpu_usage():

    result = subprocess.run(
        ["kubectl", "top", "pods"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.split("\n")[1:]

    cpu_values = []

    for line in lines:
        if line:
            cpu = line.split()[1].replace("m", "")
            cpu_values.append(int(cpu))

    return cpu_values


cpu_data = get_cpu_usage()


# Step 2: Train AI model automatically
if len(cpu_data) > 1:

    df = pd.DataFrame({
        "time": range(len(cpu_data)),
        "cpu": cpu_data
    })

    X = df[["time"]]
    y = df["cpu"]

    model = LinearRegression()
    model.fit(X, y)

    # Predict future CPU
    future_time = [[len(cpu_data) + 1]]
    prediction = model.predict(future_time)

    st.success(f"Predicted CPU usage: {int(prediction[0])} m")



    # Step 3: Show graph
    plt.figure()

    plt.plot(df["time"], df["cpu"], marker='o', label="Actual CPU")

    plt.scatter(
        len(cpu_data) + 1,
        prediction[0],
        label="Predicted CPU"
    )

    plt.legend()

    plt.title("AI CPU Prediction")

    st.pyplot(plt)


else:
    st.warning("Not enough CPU data for prediction")
