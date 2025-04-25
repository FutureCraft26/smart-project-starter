import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Dein KI-Assistent", page_icon="🤖")
st.title("👤 Personal AI Assistant")

user_input = st.text_area("Frag mich etwas:")

if st.button("Antwort generieren"):
    if user_input:
        response = client.chat.completions.create(
            model="gpt-4o",  # Du kannst auch gpt-3.5-turbo oder gpt-4 verwenden
            messages=[{"role": "user", "content": user_input}]
        )
        st.markdown("### ✨ Antwort:")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Bitte gib eine Frage ein.")
