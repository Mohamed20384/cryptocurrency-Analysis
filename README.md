# 📈 Bitcoin Price Forecasting with Machine Learning

This project is a complete pipeline for forecasting Bitcoin prices using machine learning. It includes everything from data scraping and preprocessing to modeling, evaluation, visualization, and deployment via a Streamlit dashboard.

---

## 🚀 Project Highlights

- ✅ **Automated Bitcoin data collection** via CoinGecko API  
- 🧠 **Feature engineering** for time-series modeling  
- 🔍 **Model training & evaluation** using Ridge, Random Forest, and XGBoost  
- 📊 **Interactive forecast visualization** using Streamlit  
- 📉 **Power BI dashboard** for data-driven insights  
- 🧪 Scalable design for further experimentation and extensions  

---

## 🗂️ Project Structure

```bash
bitcoin-forecasting/
│
├── data/                       # Datasets (CSV files)
│   ├── bitcoin_data.csv
│   ├── future_predictions.csv
│   └── feature_correlations.csv
│
├── models/                    # Saved models & scalers
│   ├── ridge_model.pkl
│   └── scaler.pkl
│
├── notebooks/                 # Jupyter Notebooks
│   ├── 01_data_preparation_exploration.ipynb
│   ├── 02_feature_engineering_selection.ipynb
│   ├── 03_modeling_baselines.ipynb
│   ├── 04_model_tuning_evaluation.ipynb
│   ├── 05_evaluation_reporting.ipynb
│   ├── 06_future_forecasting.ipynb
│   └── 07_streamlit_forecaster.py
│
├── .gitignore
├── README.md
└── requirements.txt
```



---

## 📊 Sample Forecast Visualization

| 📈 **30-Day Bitcoin Forecast** | ![sample_forecast](assets/sample_forecast.png) |
|-------------------------------|-----------------------------------------------|

> *Visualizes historical vs predicted prices, with adjustable forecast window.*

---

## 🧠 Feature Engineering Highlights

We create time-series-based predictive features:
- Price lag windows: `lag_1`, `lag_2`, `lag_3`, `lag_5`, `lag_7`
- Rolling averages: `ma_7`, `ma_30`
- Momentum indicators: `momentum_7`, `momentum_30`
- Volatility: `volatility_7`, `volatility_30`
- Daily return, high-low percentage, % change over 7 days

---

## 🔍 Machine Learning Models

| Model                  | R²     | MAE (USD) | MSE        |
|------------------------|--------|-----------|------------|
| ✅ Ridge Regression     | 0.845  | 1457.80   | 3.54M      |
| Random Forest          | 0.366  | 3082.84   | 14.5M      |
| XGBoost                | 0.356  | 3097.67   | 14.7M      |

---

## 🧪 Example Streamlit Dashboard

```bash
streamlit run 07_streamlit_forecaster.py
