import pandas as pd
from datetime import datetime, timedelta
import random

def fetch_aqi(city: str):
    timestamps = [datetime.now() - timedelta(hours=i) for i in range(72)]
    data = {
        "timestamp": timestamps,
        "pm25": [random.randint(50, 350) for _ in timestamps],
        "pm10": [random.randint(80, 400) for _ in timestamps],
        "no2": [random.randint(10, 80) for _ in timestamps],
        "city": city
    }
    return pd.DataFrame(data)
