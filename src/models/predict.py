import joblib
import pandas as pd
from datetime import timedelta

model = joblib.load("src/models/aqi_model.pkl")

def predict(df):
    X = df[["pm25", "pm10", "no2", "temperature", "humidity", "wind_speed"]]
    return model.predict(X)

FEATURES = ["pm25", "pm10", "no2", "temperature", "humidity", "wind_speed"]

def forecast_next_24h(last_row):
    forecasts = []
    current = last_row.copy()

    for i in range(24):
        pred = model.predict(pd.DataFrame([current[FEATURES]]))[0]
        current["aqi"] = pred

        current["timestamp"] = current["timestamp"] + timedelta(hours=1)

        # small decay assumption (can be replaced by real weather API)
        current["pm25"] *= 0.98
        current["pm10"] *= 0.98

        forecasts.append(current.copy())

    return pd.DataFrame(forecasts)
