def combine(aqi_df, weather_df):
    return aqi_df.merge(weather_df, on="timestamp", how="left")
