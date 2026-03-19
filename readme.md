<img width="1280" height="579" alt="banner" src="https://github.com/user-attachments/assets/6ad7a3d8-58d6-45be-8b8b-e72e11ea8e84" />
# 🧠 AI Fact-Checker Pipeline

[![GitHub Repo](https://img.shields.io/badge/GitHub-ai--fact--checker--pipeline-blue?logo=github)](https://github.com/grave021999/ai-fact-checker-pipeline)

This project is an **AI-powered fact-checking pipeline** that extracts claims from news data, verifies them (mock or LLM-based), and visualizes the results in an interactive Streamlit dashboard.

📍 **Live App**: [http://localhost:8501/](http://localhost:8501/) *(Will be updated once deployed to Streamlit Cloud)*  
👤 **Author**: [Mohammad Atif](https://www.linkedin.com/in/atif0201/)

---

## 📦 Features

- 🗞️ Extracts claims from real news articles
- ✅ Validates structure and format of input news data
- 🤖 Performs mock or LLM-based fact-checking
- 📊 Interactive Streamlit dashboard with:
  - Verdict distribution (pie chart)
  - Filter by verdict (True/False/Uncertain)
  - 🔍 Search box for claims
  - 📈 Time-series chart (if `pubDate` is present)
  - 💾 CSV/JSON export buttons

---

## 🚀 Setup & Run

```bash
git clone https://github.com/grave021999/ai-fact-checker-pipeline.git
cd ai-fact-checker-pipeline
pip install -r requirements.txt
streamlit run dashboard.py
Optionally configure .env with OpenAI keys if using real fact-checking via GPT.

🧪 Pipeline Steps
Ingest News → data/raw/news_rss.json

Validate → validate_news_data.py

Extract Claims → extract_claims.py

Fact-Check → fact_check_claims.py

Visualize → dashboard.py

🖼️ Preview

Example of the interactive dashboard.

📂 Project Structure
kotlin
Copy
Edit
├── data/
│   ├── raw/
│   └── processed/
├── dashboard.py
├── validate_news_data.py
├── extract_claims.py
├── fact_check_claims.py
├── requirements.txt
└── README.md
⚙️ Technologies Used
Python

Pandas

Streamlit

Plotly

tqdm

(Optional) OpenAI API

(Optional) Great Expectations

📜 License
This project is open-source for educational purposes.
