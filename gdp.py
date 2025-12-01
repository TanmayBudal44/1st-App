import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="India GDP Dashboard (2020–2025)",
    page_icon="📊",
    layout="wide",
)

# -----------------------------
# CUSTOM CSS (UI BEAUTIFICATION)
# -----------------------------
st.markdown("""
<style>
.metric-card {
    padding: 20px;
    border-radius: 14px;
    background-color: #f3f6fc;
    text-align: center;
    border: 1px solid #e0e4f1;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
}
.section-box {
    padding: 15px 20px;
    background-color: #eef2fa;
    border-radius: 12px;
    border-left: 6px solid #3f51b5;
    margin-bottom: 10px;
}
.centered-title {
    text-align: center;
    color: #2a2f4f;
    margin-bottom: -10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown("<h1 class='centered-title'>🇮🇳 India GDP Dashboard (2020–2025)</h1>", unsafe_allow_html=True)
st.markdown("<p class='centered-title'>Interactive dashboard featuring animated GDP charts and multiple visualization styles.</p>", unsafe_allow_html=True)
st.write("")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("india_gdp_2020_2025.csv")
    df["gdp_trillion_usd"] = df["gdp_current_usd"] / 1e12
    return df

df = load_data()

# -----------------------------
# METRIC CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

latest = df["gdp_trillion_usd"].iloc[-1]
start = df["gdp_trillion_usd"].iloc[0]
growth = latest - start
growth_pct = (growth / start) * 100

with col1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Latest GDP (2025)", f"{latest:.2f} T USD")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Growth Since 2020", f"{growth:.2f} T USD")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Growth %", f"{growth_pct:.1f}%")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# -----------------------------
# DATA TABLE
# -----------------------------
st.markdown("<div class='section-box'><h3>📊 GDP Data Table</h3></div>", unsafe_allow_html=True)

st.dataframe(
    df.style.format({
        "gdp_current_usd": "${:,.0f}",
        "gdp_trillion_usd": "{:.3f} T"
    }),
    use_container_width=True,
)

# -----------------------------
# MULTIPLE CHART STYLE SELECTOR
# -----------------------------
st.markdown("<div class='section-box'><h3>📈 Choose Chart Style</h3></div>", unsafe_allow_html=True)

chart_style = st.selectbox(
    "Select a visualization style:",
    ["Line Chart", "Area Chart", "Bar Chart", "Scatter Plot"]
)

if chart_style == "Line Chart":
    fig = px.line(
        df,
        x="year",
        y="gdp_trillion_usd",
        markers=True,
        title="India GDP (2020–2025) — Line Chart"
    )
    st.plotly_chart(fig, use_container_width=True)

elif chart_style == "Area Chart":
    fig = px.area(
        df,
        x="year",
        y="gdp_trillion_usd",
        title="India GDP (2020–2025) — Area Chart"
    )
    st.plotly_chart(fig, use_container_width=True)

elif chart_style == "Bar Chart":
    fig = px.bar(
        df,
        x="year",
        y="gdp_trillion_usd",
        title="India GDP (2020–2025) — Bar Chart",
        text="gdp_trillion_usd",
    )
    fig.update_traces(texttemplate='%{text:.2f}T', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

elif chart_style == "Scatter Plot":
    fig = px.scatter(
        df,
        x="year",
        y="gdp_trillion_usd",
        size="gdp_trillion_usd",
        color="year",
        title="India GDP (2020–2025) — Scatter Chart",
    )
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ANIMATED GDP CHART
# -----------------------------
st.markdown("<div class='section-box'><h3>🎞️ Animated GDP Chart (Plotly)</h3></div>", unsafe_allow_html=True)

fig_anim = px.bar(
    df,
    x="year",
    y="gdp_trillion_usd",
    animation_frame="year",
    range_y=[0, df["gdp_trillion_usd"].max() + 1],
    title="India GDP Animation (2020→2025)"
)
st.plotly_chart(fig_anim, use_container_width=True)

# -----------------------------
# PNG IMAGE (STATIC)
# -----------------------------
st.markdown("<div class='section-box'><h3>🖼️ Saved PNG Chart</h3></div>", unsafe_allow_html=True)
st.image("india_gdp_2020_2025.png", use_column_width=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
---
### 📚 Data Sources  
- World Bank — GDP (Current USD)  
- IMF WEO — 2025 Projection  
- TradingEconomics, Macrotrends (Cross-verified)  

### 🎨 Features  
- Animated GDP Chart (Plotly)  
- Multiple Chart Styles  
- Modern Dashboard UI/UX  
- Fully Streamlit Cloud Compatible  
""")


