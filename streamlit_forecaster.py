import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bitcoin Price Forecast", layout="centered")

st.title("📈 Bitcoin Price Forecast Dashboard")
st.markdown("Visualize predicted Bitcoin prices for the upcoming days using your trained regression model.")

@st.cache_data
def load_data():
    forecast = pd.read_csv("future_predictions.csv", parse_dates=True, index_col=0)
    forecast.index.name = "date"

    history = pd.read_csv("bitcoin_data.csv", parse_dates=["date"])
    history.set_index("date", inplace=True)

    return forecast, history

forecast_df, history_df = load_data()

st.sidebar.header("🔧 Settings")
forecast_days = st.sidebar.slider("Forecast Horizon (days)", min_value=7, max_value=len(forecast_df), value=30)
show_history = st.sidebar.checkbox("Overlay Historical Data", value=True)
history_days = st.sidebar.slider("Days of History to Show", min_value=30, max_value=180, value=60)

st.subheader(f"Forecast for the Next {forecast_days} Days")

fig, ax = plt.subplots(figsize=(12, 6))

if show_history:
    historical_slice = history_df['price'].iloc[-history_days:]
    ax.plot(historical_slice.index, historical_slice.values, label="Historical Price", linewidth=2, color='blue')

forecast_slice = forecast_df.iloc[:forecast_days]
ax.plot(forecast_slice.index, forecast_slice['predicted_price'], label="Forecasted Price", linestyle="--", color='green')

ax.set_title("Bitcoin Price Forecast", fontsize=16)
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.grid(True)
ax.legend()

st.pyplot(fig)

with st.expander("📄 Show Forecast Table"):
    st.dataframe(forecast_df.head(forecast_days), use_container_width=True)

st.markdown("---")