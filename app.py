import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="AI Study Management", layout="centered")

st.title("AI Study Management System")

# Sidebar
st.sidebar.header("Settings")
MODEL_NAME = st.sidebar.selectbox(
    "Model",
    ["gpt-4o-mini"]
)

TEMPERATURE = st.sidebar.slider("Temperature", 0.0, 1.0, 0.3)
MAX_TOKENS = st.sidebar.slider("Max Tokens", 100, 2000, 800)

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Prompt functions
def generate_response(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content

# Tabs
tab1, tab2, tab3 = st.tabs(["Summary", "Flashcards", "Quiz"])

text = st.text_area("Enter your study text here", height=200)

with tab1:
    if st.button("Generate Summary"):
        if text.strip():
            with st.spinner("Generating summary..."):
                st.success(generate_response(f"Summarize this text:\n{text}"))

with tab2:
    if st.button("Generate Flashcards"):
        if text.strip():
            with st.spinner("Generating flashcards..."):
                st.success(generate_response(
                    f"Generate flashcards in Q&A format:\n{text}"
                ))

with tab3:
    if st.button("Generate Quiz"):
        if text.strip():
            with st.spinner("Generating quiz..."):
                st.success(generate_response(
                    f"Generate MCQ questions:\n{text}"
                ))
