import streamlit as st
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Lade Umgebungsvariablen
load_dotenv()

# OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Dateipfad zum Speichern der Konversationen
memory_file = 'chat_memory.json'

# Lade den Verlauf aus der Datei
def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, 'r') as f:
            return json.load(f)
    else:
        return {"memory": []}

# Speichere den Verlauf in die Datei
def save_memory(memory):
    with open(memory_file, 'w') as f:
        json.dump(memory, f)

# Initialisiere das Chat-Gespräch
st.set_page_config(page_title="🤖 Dein KI-Assistent")
st.title("🤖 Personal AI Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_memory()["memory"]

user_input = st.text_input("Schreib mir etwas...")

# Wenn der Benutzer eine Eingabe macht
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Hole Antwort von OpenAI
    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.chat_history
    )
    
    assistant_message = response['choices'][0]['message']['content']
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

    # Speicher den Verlauf
    save_memory({"memory": st.session_state.chat_history})

# Zeige den Verlauf der Unterhaltung
for msg in st.session_state.chat_history:
    role_class = "user" if msg["role"] == "user" else "assistant"
    st.markdown(f'<div class="message-bubble {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)

