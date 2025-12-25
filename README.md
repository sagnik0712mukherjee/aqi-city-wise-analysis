# 🌫️ AI City-wise AQI Prediction Platform 🇮🇳

An end-to-end **AI-powered real-time Air Quality Intelligence Platform** for Indian cities, combining:

- 📊 Machine Learning–based AQI prediction  
- ⏭️ **Next 24-hour AQI forecasting**
- 🧠 **GPT-5-mini–powered AI analysis & RAG**
- 🗺️ **City heatmaps**
- 🧑‍⚕️ **Personalized health advice**
- 🎛️ Interactive **Streamlit dashboard**

Built with a strong focus on **interpretability, real-time insights, and public health impact**.

---

## 🚀 Key Capabilities

### 🌆 City-wise AQI Intelligence
- Fetches real-time AQI & weather data
- Supports multiple Indian metro cities
- Combines pollution + meteorological signals

### 📈 AQI Prediction & Forecasting
- ML-based AQI prediction
- **Next 24-hour forecast horizon**
- Time-series visualization of AQI trends

### 🧠 Explainable AI
- Model explainability for *why AQI is high*
- Feature-level reasoning (pollutants, weather, trends)

### 🤖 AI AQI Expert (RAG + GPT-5-mini)
- Ask questions like:
  - *“Why is Delhi AQI high today?”*
  - *“Is it safe to jog tomorrow morning?”*
- Uses Retrieval-Augmented Generation over AQI knowledge

### 🗺️ AQI Heatmaps
- Live city-level AQI heat visualization
- Geospatial awareness using latitude/longitude mapping

### 🧑‍⚕️ Personalized Health Advisory
- Age-aware recommendations
- Special handling for asthma / respiratory conditions
- Dynamic risk-based guidance

---

## 🗂️ Repository Structure

```text
aqi-city-wise-analysis/
├── src/
│   ├── data_pipeline/              # Data ingestion & preprocessing
│   │   ├── fetch_aqi.py
│   │   ├── fetch_weather.py
│   │   └── combine_data.py
│   │
│   ├── feature_engineering/        # Feature creation
│   │   └── features.py
│   │
│   ├── models/                     # ML models
│   │   ├── train_model.py
│   │   └── predict.py              # Prediction + 24h forecasting
│   │
│   ├── explainability/             # Explainable AI layer
│   │   └── explain.py
│   │
│   ├── rag/                        # RAG + GPT-5-mini AQI assistant
│   │   ├── documents.py
│   │   └── aqi_chat.py
│   │
│   └── data/                       # Sample / cached data
│       └── sample_aqi.csv
│
├── config/
│   └── settings.py                 # API keys, city coordinates, constants
│
├── streamlit_app.py                # Streamlit UI
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

### 📄 Sample Data (`sample_aqi.csv`)

This file is used for local testing, development, and model bootstrapping.

**Expected CSV schema:**
```csv
timestamp,city,aqi,pm2_5,pm10,no2,so2,co,o3,temperature,humidity,wind_speed
```

**Example row:**
```text
2025-01-01 10:00:00,Delhi,312,185,290,78,12,1.4,34,18.2,61,3.5
```

### 🖥️ Streamlit Dashboard Features
- ✅ City selector dropdown
- ✅ AQI trend line charts
- ✅ Next 24-hour AQI forecast
- ✅ Explainable AI insights
- ✅ AI-powered AQI Q&A chatbot
- ✅ City-wise AQI heatmaps
- ✅ Personalized health recommendations

### ⚙️ Installation & Run
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
export OPENAI_API_KEY=your_openai_key

# Run Streamlit app
streamlit run streamlit_app.py
```

### 🧠 Tech Stack
- **Languages**: Python
- **ML/DS**: Scikit-learn, XGBoost, Pandas, NumPy
- **Frontend**: Streamlit
- **LLM/AI**: OpenAI GPT-5-mini, RAG (Retrieval-Augmented Generation)
- **Interpretability**: Explainable AI (SHAP-style reasoning)

### 🎯 Use Cases
- Public AQI awareness platforms
- Smart city air quality monitoring
- Health-risk advisory systems
- Environmental research and policy analysis
- Portfolio-grade AI + ML project

---

### 👤 Author
**Sagnik Mukherjee**
- 🔗 GitHub: [sagnik0712mukherjee](https://github.com/sagnik0712mukherjee)
