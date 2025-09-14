import streamlit as st
import json
import os

st.set_page_config(page_title="AI for PMs Assistant", layout="wide")

st.title("🧠 AI for PMs Assistant")
st.markdown("Helping project managers understand technical concepts — in plain English.")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["Concept Explorer", "GPT Q&A"])

# Load concept data
DATA_PATH = os.path.join("data", "concepts.json")
with open(DATA_PATH, "r") as f:
    concepts = json.load(f)

# Concept Explorer Page
if page == "Concept Explorer":
    st.header("📘 Concept Explorer")
    st.markdown("Search and explore key technical terms — explained for PMs.")

    search_input = st.text_input("Enter a tech term (e.g., API, CI/CD, Load Balancer)").strip().lower()

    import streamlit as st
import json
import os
# Normalize search input
query = search_input.strip().lower()
found = None

# Match search input to a concept via aliases
for key, concept in concepts.items():
    aliases = concept.get("aliases", [])
    if query in aliases:
        found = concept
        break

if found:
    st.markdown("---")
    st.markdown(
        f"""
        <div style="
            border:1px solid #ccc;
            border-radius:8px;
            padding:16px;
            background-color:#f3e8ff;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.08);
            color:#222;
            font-family: 'Segoe UI', sans-serif;
        ">
            <h3 style="margin-bottom: 8px; color:#4b0082;">🧠 {found['term']}</h3>
            <p><strong>Definition:</strong> {found['definition']}</p>
            <p><strong>In Real Projects:</strong> {found['project_use']}</p>
            <p><strong>PM Tip:</strong> {found['pm_tip']}</p>
            <p><strong>Metaphor:</strong> {found['metaphor']}</p>
            <p><strong>Learn More:</strong></p>
            <ul>
                {''.join([f'<li><a href="{link}" target="_blank">{name}</a></li>' for name, link in found["links"]])}
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
elif search_input:
    st.warning("❌ This term hasn't been added yet. Try 'API', 'CI/CD', 'AI', or 'Cloud'.")

# GPT Q&A Page (placeholder)
elif page == "GPT Q&A":
    st.header("🤖 Ask the Assistant")
    st.markdown("This feature will allow you to ask technical questions and get GPT-powered answers.")
    st.info("Coming soon: live GPT answers")
