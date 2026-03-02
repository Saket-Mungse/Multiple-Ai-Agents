# 🤖 Multi-Agent AI System

This is a Multi-Agent AI application built using Python and Google Gemini API.

The system contains multiple specialized AI agents that handle different types of queries.

## 🧠 Available Agents

- 👔 Career Agent – Jobs, salary, resume, interviews
- 🥗 Diet Agent – Nutrition and meal planning
- 📄 Summary Agent – Text summarization
- 💻 Coding Agent – Programming help
- 🎯 Prompt Generation Agent – Creates structured prompts

The project includes:
- CLI version (`main.py`)
- Streamlit Web UI (`app.py`)
- Modular AI pipeline (`pipeline.py`)

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install streamlit google-generativeai
🔑 Add Your API Key

Open gemini_config.py and replace:

client = genai.Client(api_key="YOUR_API_KEY")

With your actual Gemini API key.

▶️ Run CLI Version
python main.py
🌐 Run Streamlit Web App
streamlit run app.py

Open browser at:

http://localhost:8501
