import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CITY_LIST = ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai"]

CITY_COORDS = {
    "Delhi": [28.6139, 77.2090],
    "Mumbai": [19.0760, 72.8777],
    "Bangalore": [12.9716, 77.5946],
    "Kolkata": [22.5726, 88.3639],
    "Chennai": [13.0827, 80.2707],
}

AQI_FORECAST_HOURS = 24
