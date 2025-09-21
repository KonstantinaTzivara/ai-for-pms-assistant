[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-purple?logo=streamlit)](https://ai-for-pms-assistant-ascqbepwymm6szh5jobz82.streamlit.app/)

# 🧠 AI for PMs Assistant

A practical, AI-powered tool that helps **project managers** understand technical concepts in context.

---

## 👩‍💼 What It Is

AI for PMs is a lightweight learning assistant designed for **non-technical project managers** who want to make sense of technical terms like `APIs`, `cloud`, or `DevOps` — without drowning in jargon.

It blends **static explanations** and **on-demand Q&A**, all tailored for real-world project environments.

This is a personal project to showcase:
- Technical understanding
- Realistic feature planning (Jira + Confluence)
- AI integration (OpenAI GPT models)
- Practical PM tooling in SaaS/consulting environments

---

## 🔍 Try It Live

🌐 [Live App on Streamlit Cloud](https://ai-for-pms-assistant-ascqbepwymm6szh5jobz82.streamlit.app/)  
📝 [Confluence Page](#)  
🗂️ [Jira Board / Backlog](#)

---

## 🧠 Features

### ✅ Concept Explorer (Static)

Search for terms like `API Gateway`, `CI/CD`, or `Load Balancer` and get:

- A clear, simple explanation
- How the term appears in real projects
- What a PM should know or ask
- A metaphor to make it stick
- Links to trusted docs (AWS, MDN, Azure, etc.)

💡 Built with:
- `Streamlit` frontend
- `JSON` concept file (scalable)
- PM-friendly, clean UI

---

### 🔐 GPT Q&A Module

Ask any tech question and get a GPT-powered answer designed for PMs.

✅ Features:
- Free-text input (e.g. *What is an API Gateway?*)
- Project-focused GPT response (short, clear, structured)
- Password protection to limit usage
- Token quota per password (configurable)

⚠️ Passwords are stored in `secrets.toml` for security.  
The `allowed_passwords.json` approach has been **replaced** with a secrets-based method (works better on Streamlit Cloud).

---

## 🔧 Tech Stack

- **Frontend**: Streamlit
- **Language**: Python
- **Data**: JSON (concept content)
- **AI Backend**: OpenAI `gpt-3.5-turbo`
- **Planning**: Jira + Confluence
- **Hosting**: Streamlit Cloud

---

## 📁 File Structure

```bash
📂 ai-for-pms-assistant
├── app.py
├── data/
│   └── concepts.json
├── .streamlit/
│   └── secrets.toml (not committed)
├── requirements.txt
├── README.md
