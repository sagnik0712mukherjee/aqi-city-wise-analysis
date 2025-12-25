def add_features(df):
    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.dayofweek
    df["aqi"] = (
        0.5 * df["pm25"] +
        0.3 * df["pm10"] +
        0.2 * df["no2"]
    )
    return df
