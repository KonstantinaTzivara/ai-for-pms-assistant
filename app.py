import streamlit as st
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

st.markdown("""
<style>
/* BUTTON ROW */
.button-row {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 30px;
}

.pm-button {
    background-color: #8b5cf6;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 18px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    min-width: 160px;
    height: 48px;
    text-align: center;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
    transition: background-color 0.2s ease;
}

.pm-button:hover {
    background-color: #7c3aed;
}

/* TEXT SELECTION */
::selection {
    background: #d1b3ff;
    color: black;
}

/* GLOBAL BUTTON OVERRIDES */
button, .stButton > button {
    background-color: #7b2cbf;
    color: white;
    border: 1px solid #d1b3ff;
    border-radius: 6px;
}

button:hover, .stButton > button:hover {
    background-color: #9d4edd;
    color: white;
    border: 1px solid #ffffff;
}

/* SELECT DROPDOWN STYLE */
.css-1d391kg, .stSelectbox, .stSelectbox div {
    border-color: #d1b3ff !important;
    background-color: #1e1e1e !important;
    color: white !important;
}

.css-1cpxqw2:focus, .css-1cpxqw2:hover {
    border-color: #9d4edd !important;
    box-shadow: 0 0 0 0.2rem rgba(125, 86, 255, 0.25) !important;
}

/* CARD STYLES */
.card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    background-color: #f3e8ff;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.08);
    color: #222;
    font-family: 'Segoe UI', sans-serif;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)




load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load allowed passwords
with open("data/allowed_passwords.json", "r") as f:
    allowed_passwords = json.load(f)

# Session state init
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["password"] = ""
    st.session_state["quota_remaining"] = 0

st.set_page_config(page_title="AI for PMs Assistant", layout="wide")

st.title("🧠 AI for PMs Assistant")
st.markdown("Helping project managers understand technical concepts in plain English.")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["Concept Explorer", "GPT Q&A"])

# Load concept data
DATA_PATH = os.path.join("data", "concepts.json")
with open(DATA_PATH, "r") as f:
    concepts = json.load(f)

# Concept Explorer Page
if page == "Concept Explorer":
    st.markdown("### 📚 Concept Explorer")
    st.markdown("Use the dropdown below or start typing to quickly find a tech term.")

    term_options = sorted(
        [concept["term"] for concept in concepts.values()],
        key=lambda x: x.lower()
    )

    selected_term = st.selectbox(
        "🔍 Select a tech term to explore",
        options=[""] + term_options,  # Add blank first
        format_func=lambda x: "Please select a term" if x == "" else x
    )

    found = None
    if selected_term:
        for concept in concepts.values():
            if concept["term"] == selected_term:
                found = concept
                break

    if found:
        st.markdown(f"""
        <div class="card">
            <h4>{found['term']}</h4>
            <p><strong>🧠 Definition:</strong> {found['definition']}</p>
            <p><strong>📌 Project Use:</strong> {found['project_use']}</p>
            <p><strong>💡 PM Tip:</strong> {found['pm_tip']}</p>
            <p><strong>🎯 Metaphor:</strong> {found['metaphor']}</p>
            <p><strong>🔗 Links:</strong></p>
            <ul>
                {''.join([f'<li><a href="{url}" target="_blank">{label}</a></li>' for label, url in found['links']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class='card'>
            👋 Welcome! Use the dropdown above to explore tech concepts explained in plain English.
        </div>
        """, unsafe_allow_html=True)


elif page == "GPT Q&A":
    # Initialize session state variables
    for key, default in {
        "authenticated": False,
        "password": "",
        "quota_remaining": 0,
        "trigger_submit": False,
        "selected_question": "",
        "last_response": ""
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    st.header("🤖 Ask the Assistant")
    st.caption("This assistant helps project managers understand technical concepts in plain English.")
    st.markdown("### Not sure what to ask? Try one of these:")

    # Example buttons
    example_questions = [
        "What is an API? What should a PM know about it?",
        "What is the difference between frontend and backend?",
        "Explain CI/CD in simple terms.",
        "What is agile methodology?"
    ]

    # Display example question buttons
    buttons_html = '<div class="button-row">'
    for i, q in enumerate(example_questions):
        button_key = f"example_button_{i}"
        if st.button(q, key=button_key):
            st.session_state["selected_question"] = q
            st.session_state["trigger_submit"] = True
    buttons_html += '</div>'
    st.markdown(buttons_html, unsafe_allow_html=True)
    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)  # Spacer

    # Input field
    with st.container():
        col1, col2 = st.columns([6, 1])
        with col1:
            question = st.text_input(
                "Enter your question",
                placeholder="e.g. What is a load balancer?",
                label_visibility="collapsed",
                value=st.session_state.get("selected_question", "")
            )
        with col2:
            if st.button("Ask"):
                st.session_state["selected_question"] = question
                st.session_state["trigger_submit"] = True

    # Password form
    if not st.session_state["authenticated"]:
        with st.form("password_form"):
            password_input = st.text_input("🔐 Enter password to use assistant:", type="password")
            submit_pw = st.form_submit_button("Submit")
            if submit_pw:
                if password_input in allowed_passwords:
                    st.session_state["authenticated"] = True
                    st.session_state["password"] = password_input
                    st.session_state["quota_remaining"] = allowed_passwords[password_input]
                    st.success(f"✅ Access granted. You have {allowed_passwords[password_input]} queries.")
                else:
                    st.error("❌ Invalid password. Please try again.")

    # Process query if authenticated and allowed
    if st.session_state["authenticated"]:
        if st.session_state["quota_remaining"] <= 0:
            st.warning("⚠️ Query limit reached for this password.")
        elif st.session_state.get("trigger_submit") and st.session_state.get("selected_question", "").strip():
            question = st.session_state["selected_question"].strip()
            st.session_state["trigger_submit"] = False
            with st.spinner("Thinking..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant for project managers trying to understand technical concepts."},
                            {"role": "user", "content": question}
                        ]
                    )
                    st.session_state["last_response"] = response.choices[0].message.content
                    st.session_state["quota_remaining"] -= 1
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

        # Display GPT result if available
        if st.session_state.get("last_response"):
            st.markdown("---")
            st.markdown(f"""
                <div class="card">
                    {st.session_state['last_response']}
                </div>
            """, unsafe_allow_html=True)



