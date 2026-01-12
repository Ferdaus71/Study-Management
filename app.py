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

# Response generator
def generate_response(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(
    ["Summary", "Flashcards", "Quiz", "Answer Evaluation"]
)

# Input text
text = st.text_area("Enter your study text here", height=200)

# Summary
with tab1:
    if st.button("Generate Summary"):
        if text.strip():
            with st.spinner("Generating summary..."):
                st.success(
                    generate_response(
                        f"Summarize the following study notes clearly and concisely:\n{text}"
                    )
                )

# Flashcards
with tab2:
    if st.button("Generate Flashcards"):
        if text.strip():
            with st.spinner("Generating flashcards..."):
                st.success(
                    generate_response(
                        f"""
Generate flashcards from the following text.
Return the output in clear question–answer format.

Text:
{text}
"""
                    )
                )

# Quiz
with tab3:
    if st.button("Generate Quiz"):
        if text.strip():
            with st.spinner("Generating quiz..."):
                st.success(
                    generate_response(
                        f"""
Generate multiple-choice questions from the following text.
Each question must have four options and one correct answer.

Text:
{text}
"""
                    )
                )

# Answer Evaluation
with tab4:
    correct_answer = st.text_area("Correct Answer", height=100)
    user_answer = st.text_area("User Answer", height=100)

    if st.button("Evaluate Answer"):
        if correct_answer.strip() and user_answer.strip():
            with st.spinner("Evaluating answer..."):
                st.success(
                    generate_response(
                        f"""
Evaluate the user's answer based on the correct answer.

Correct Answer:
{correct_answer}

User Answer:
{user_answer}

Return the evaluation strictly in JSON format:
{{
  "score": 0-100,
  "feedback": "short and clear feedback"
}}
"""
                    )
                )
