import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Dein KI-Assistent", page_icon="🤖")

st.title("👤 Personal AI Assistant")
user_input = st.text_area("Frag mich etwas:")

if st.button("Antwort generieren"):
    if user_input:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # oder "gpt-4"
            messages=[{"role": "user", "content": user_input}]
        )
        st.markdown("### ✨ Antwort:")
        st.write(response["choices"][0]["message"]["content"])
    else:
        st.warning("Bitte gib zuerst eine Frage ein!")
