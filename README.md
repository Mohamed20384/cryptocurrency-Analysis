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
