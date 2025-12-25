import joblib
from sklearn.ensemble import RandomForestRegressor

def train(df):
    X = df[["pm25", "pm10", "no2", "temperature", "humidity", "wind_speed"]]
    y = df["aqi"]

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X, y)

    joblib.dump(model, "src/models/aqi_model.pkl")
    return model
