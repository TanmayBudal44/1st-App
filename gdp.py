# Streamlit app to display India GDP (2020-2025)
# Save this file as app.py and run: streamlit run app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("India Nominal GDP (Current US$) — 2020 to 2025")

# Load data
df = pd.read_csv("india_gdp_2020_2025.csv")
df["gdp_trillion_usd"] = df["gdp_current_usd"] / 1e12

st.subheader("Data (table)")
st.dataframe(df.style.format({"gdp_current_usd":"${:,.0f}", "gdp_trillion_usd":"{:.3f} T"}))

st.subheader("Line chart")
fig, ax = plt.subplots(figsize=(9,5))
ax.plot(df["year"], df["gdp_trillion_usd"], marker='o')
ax.set_xlabel("Year")
ax.set_ylabel("GDP (Trillion US$)")
ax.set_title("India Nominal GDP (Current US$) — 2020 to 2025")
ax.grid(True)
st.pyplot(fig)

st.markdown("**Sources:** World Bank (GDP current US$ 2020-2024), IMF WEO (2025 projection), TradingEconomics / Worldometers / Macrotrends (for cross-checking).")
