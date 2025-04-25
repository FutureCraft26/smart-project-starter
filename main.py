import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initial page config
st.set_page_config(
    page_title="🧠 Dein KI-Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .message-bubble {
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 1rem;
        background-color: #1a1a1a;
        color: white;
    }
    .user {
        background-color: #3a3a3a;
        text-align: right;
    }
    .bot {
        background-color: #2b2b2b;
        text-align: left;
    }
    .stTextArea textarea {
        font-size: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Personal AI Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Schreib mir etwas...")

if user_input:
    # Speichere Nutzer-Nachricht
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Anfrage an OpenAI
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.chat_history
    )
    bot_message = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": bot_message})

# Anzeige der Konversation
for msg in reversed(st.session_state.chat_history):
    with st.container():
        role_class = "user" if msg["role"] == "user" else "bot"
        st.markdown(f'<div class="message-bubble {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)
