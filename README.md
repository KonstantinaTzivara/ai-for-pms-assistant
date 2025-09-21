[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-purple?logo=streamlit)](https://ai-for-pms-assistant-ascqbepwymm6szh5jobz82.streamlit.app/)

ai-for-pms-assistant
A practical AI-powered tool that helps project managers understand tech concepts in context
 AI for PMs Assistant

👩‍💼 What It Is

AI for PMs is a simple, AI-powered tool designed to help **non-technical project managers** understand complex tech concepts — like APIs, cloud, or machine learning — in **plain English and real project context**.

This is my personal project to showcase:
- Technical thinking
- Project management planning (Jira + Confluence)
- Usability for real-world SaaS/consulting roles
- AI integration with GPT models


🔍 Demo

🌐 [Live App on Streamlit Cloud](https://ai-for-pms-assistant-ascqbepwymm6szh5jobz82.streamlit.app/)
📝 [Confluence Page](#)  
🗂️ [Jira Backlog (sample board)](#)

(*Links will be updated as I build it*)

 🧠 Why I Built This

I noticed that many PMs struggle to follow technical discussions or ask the right questions. This tool helps them:
- Understand concepts **on demand**
- See how tech terms show up **in real projects**
- Build confidence and bridge the gap with developers


💡 What It Does (MVP)

✅ Concept Explorer  
Search tech terms like `API` or `Load Balancer` and see:
- A short, plain-English definition
- How it appears in real projects
- What a PM should ask or know
- A metaphor to make it stick
- Links to trusted documentation (AWS, MDN, etc.)

Built using:
- `Streamlit` for frontend
- `JSON` file for data structure (scalable for new concepts)
- Clean, PM-first UX with clarity and focus


 🛠️ Tech Stack

- Frontend: **Streamlit**
- Data: **JSON**
- Language: **Python**
- Planning: Jira + Confluence (linked below)



 📷 Demo

🎥 Coming soon: Loom video walkthrough

---

## 🔐 GPT Q&A Module (New Feature)

This assistant helps project managers understand technical concepts using GPT-3.5.

Access is password-protected. Each password allows **up to 10 GPT queries**.

📌 To test the assistant:
- Go to the **GPT Q&A** page
- Enter a temporary password (provided on request)
- Start asking questions

Note: The `allowed_passwords.json` file is **excluded from the repo** for security reasons.

---

---

 📁 File Structure

```bash
📂 ai-for-pms-assistant
├── app.py
├── data/
│   └── concepts.json
├── requirements.txt
├── .env (not committed)


 📃 License

MIT License – free to use, modify, or build on!
