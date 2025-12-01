import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STREAMLIT APP TITLE & INTRO
# -----------------------------
st.title("🇮🇳 India GDP Visualization (2020–2025)")
st.markdown("""
This app shows India's **Nominal GDP (in Trillion USD)** from **2020 to 2025**, using official  
World Bank, IMF projections, and cross-verified public datasets.
""")

# -----------------------------
# LOAD THE CSV FILE
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("india_gdp_2020_2025.csv")
    df["gdp_trillion_usd"] = df["gdp_current_usd"] / 1e12
    return df

df = load_data()

# -----------------------------
# SHOW DATA TABLE
# -----------------------------
st.subheader("📊 GDP Data Table")
st.dataframe(
    df.style.format({
        "gdp_current_usd": "${:,.0f}",
        "gdp_trillion_usd": "{:.3f} T"
    })
)

# -----------------------------
# MATPLOTLIB CHART
# -----------------------------
st.subheader("📈 GDP Line Chart (Matplotlib)")

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(df["year"], df["gdp_trillion_usd"], marker="o")
ax.set_xlabel("Year")
ax.set_ylabel("GDP (Trillion USD)")
ax.set_title("India Nominal GDP (2020–2025)")
ax.grid(True)

st.pyplot(fig)

# -----------------------------
# OPTIONAL: SHOW PNG FILE
# -----------------------------
st.subheader("🖼️ Pre-Generated GDP Chart Image (PNG from repo)")
st.image("india_gdp_2020_2025.png", caption="India GDP Chart (2020–2025)")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
---
### 📌 Data Sources  
- **World Bank** GDP (Current USD)  
- **IMF WEO 2025** (Projection)  
- Cross-verified with **Worldometers, TradingEconomics, Macrotrends**

### 💡 Notes  
- Make sure `india_gdp_2020_2025.csv` and `india_gdp_2020_2025.png` are in the **same GitHub folder** as `app.py` before deploying to streamlit.io.
""")

