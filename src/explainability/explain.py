def explain_prediction(row):
    reasons = []
    if row.pm25 > 200:
        reasons.append("High PM2.5 concentration")
    if row.wind_speed < 1:
        reasons.append("Low wind speed trapping pollutants")
    if row.humidity > 70:
        reasons.append("High humidity worsening air quality")

    return ", ".join(reasons) if reasons else "Moderate atmospheric conditions"


def personalized_advice(aqi, age, asthma):
    if aqi > 300:
        advice = "Avoid going outside. Wear N95 mask indoors if possible."
    elif aqi > 200:
        advice = "Limit outdoor exposure. Use air purifier if available."
    else:
        advice = "Air quality is moderate. Outdoor activity is acceptable."

    if age < 12 or age > 60:
        advice += " Extra caution advised due to age."
    if asthma:
        advice += " Asthma patients should strictly avoid outdoor activity."

    return advice
