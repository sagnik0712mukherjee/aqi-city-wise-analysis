import pandas as pd
import random

def fetch_weather(city: str, timestamps):
    return pd.DataFrame({
        "timestamp": timestamps,
        "temperature": [random.uniform(15, 40) for _ in timestamps],
        "humidity": [random.randint(30, 90) for _ in timestamps],
        "wind_speed": [random.uniform(0.5, 5) for _ in timestamps],
    })
