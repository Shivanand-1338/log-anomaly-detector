import streamlit as st
from preprocessing import load_logs, vectorize_logs
from model import train_anomaly_detector
import pandas as pd

st.title("Real-time Log Anomaly Detector")

logs = load_logs()
X, vectorizer = vectorize_logs(logs)
model = train_anomaly_detector(X)

preds = model.predict(X)  # -1 = anomaly, 1 = normal

df = pd.DataFrame({
    "Log": logs,
    "Status": ["Anomaly" if p == -1 else "Normal" for p in preds]
})

st.dataframe(df.style.apply(lambda x: ["background-color: red" if v == "Anomaly" else "" for v in x], subset=["Status"]))