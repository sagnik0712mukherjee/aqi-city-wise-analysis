import streamlit as st
import pandas as pd

# ===================== Imports =====================
from src.data_pipeline.fetch_aqi import fetch_aqi
from src.data_pipeline.fetch_weather import fetch_weather
from src.data_pipeline.combine_data import combine
from src.feature_engineering.features import add_features
from src.models.train_model import train
from src.models.predict import predict, forecast_next_24h
from src.explainability.explain import explain_prediction, personalized_advice
from src.rag.aqi_chat import chat
from config.settings import CITY_COORDS

# ===================== Page Config =====================
st.set_page_config(
    page_title="AI AQI Predictor 🇮🇳",
    layout="wide"
)

st.title("🌫️ AI-Powered AQI Prediction Platform")
st.caption(
    "Real-time AQI prediction, 24h forecasting, explainability, maps, and personalized health advice"
)

# ===================== Sidebar =====================
st.sidebar.header("⚙️ Controls")

city = st.sidebar.selectbox(
    "Select City",
    list(CITY_COORDS.keys())
)

run_btn = st.sidebar.button("🚀 Run AQI Analysis")

# ===================== Session State =====================
if "df" not in st.session_state:
    st.session_state.df = None

# ===================== DATA PIPELINE =====================
if run_btn:
    with st.spinner("Fetching data & running models..."):
        aqi_df = fetch_aqi(city)
        weather_df = fetch_weather(city, aqi_df["timestamp"])
        df = combine(aqi_df, weather_df)
        df = add_features(df)

        train(df)
        df["predicted_aqi"] = predict(df)

        st.session_state.df = df

# ===================== MAIN DASHBOARD =====================
if st.session_state.df is not None:
    df = st.session_state.df

    col1, col2 = st.columns(2)

    # ---------- AQI Trend ----------
    with col1:
        st.subheader("📈 AQI Trend (Historical)")
        st.line_chart(
            df.set_index("timestamp")["predicted_aqi"]
        )

    # ---------- Explainability ----------
    with col2:
        st.subheader("🧠 Why AQI is High?")
        st.info(
            explain_prediction(df.iloc[-1])
        )

    # ===================== FORECAST =====================
    st.subheader("⏭️ AQI Forecast (Next 24 Hours)")

    forecast_df = forecast_next_24h(df.iloc[-1])
    st.line_chart(
        forecast_df.set_index("timestamp")["aqi"]
    )

    # ===================== MAP =====================
    st.subheader("🗺️ City-wise AQI Heatmap")

    map_rows = []
    for c, (lat, lon) in CITY_COORDS.items():
        map_rows.append([lat, lon, df["aqi"].iloc[-1]])

    map_df = pd.DataFrame(
        map_rows,
        columns=["lat", "lon", "aqi"]
    )

    st.map(map_df)

    # ===================== HEALTH ADVICE =====================
    st.subheader("🧑‍⚕️ Personalized Health Advice")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 1, 90, 30)

    with col2:
        asthma = st.checkbox("Asthma / Respiratory issues")

    with col3:
        get_advice = st.button("Get Advice")

    if get_advice:
        advice = personalized_advice(
            df.iloc[-1]["aqi"],
            age,
            asthma
        )
        st.warning(advice)

    # ===================== AI CHAT =====================
    st.divider()
    st.subheader("💬 Ask AQI Expert (AI)")

    query = st.text_input(
        "Ask about AQI, health risks, or pollution trends"
    )

    if query:
        with st.spinner("Thinking..."):
            response = chat(
                query,
                context=f"City: {city}, AQI: {df.iloc[-1]['aqi']:.2f}"
            )
            st.success(response)

else:
    st.info("👈 Select a city and click **Run AQI Analysis** to begin.")