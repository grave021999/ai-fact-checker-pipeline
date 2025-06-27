import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="Fact-Checker Dashboard", layout="wide")
st.title("🧠 Fact-Checker Dashboard")
st.markdown("### 📊 Fact Check Result Distribution")

# Load data
data_path = "data/processed/claims_fact_checked.json"
try:
    df = pd.read_json(data_path)
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# Extract "verdict" from "fact_check_result"
df["verdict"] = df["fact_check_result"].str.extract(r'^(True|False|Uncertain)', expand=False)

# -------------------- 🎛️ Filters --------------------

col1, col2 = st.columns([1, 2])

# Filter by verdict
verdict_filter = col1.selectbox("Filter by Verdict", ["All", "True", "False", "Uncertain"])
if verdict_filter != "All":
    df = df[df["verdict"] == verdict_filter]

# Search by claim text
search_term = col2.text_input("🔍 Search Claims", "")
if search_term:
    df = df[df["claim"].str.contains(search_term, case=False)]

# -------------------- 📊 Pie Chart --------------------
result_counts = df["verdict"].value_counts().reset_index()
result_counts.columns = ["Fact-Check Result", "Count"]

if not result_counts.empty:
    fig = px.pie(
        result_counts,
        names="Fact-Check Result",
        values="Count",
        title="Fact-Check Verdict Breakdown",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No matching results to show.")

# -------------------- 📈 Time Series (if pubDate exists) --------------------
if "pubDate" in df.columns:
    df["pubDate"] = pd.to_datetime(df["pubDate"], errors="coerce")
    time_counts = df.dropna(subset=["pubDate"]).groupby(df["pubDate"].dt.date).size().reset_index(name="Counts")

    st.markdown("### 🕒 Claims Over Time")
    fig_time = px.line(
        time_counts,
        x="pubDate",
        y="Counts",
        markers=True,
        title="Number of Claims by Date"
    )
    st.plotly_chart(fig_time, use_container_width=True)

# -------------------- 📁 Data & Export --------------------
st.markdown("### 📄 Fact-Checked Claims")
st.dataframe(df[["claim", "fact_check_result"]], use_container_width=True)

csv_data = df.to_csv(index=False).encode("utf-8")
json_data = df.to_json(orient="records", indent=2).encode("utf-8")

col_csv, col_json = st.columns(2)
col_csv.download_button("⬇️ Export as CSV", csv_data, "claims_filtered.csv", "text/csv")
col_json.download_button("⬇️ Export as JSON", json_data, "claims_filtered.json", "application/json")
