import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (for local use)
load_dotenv()

# Page configuration
st.set_page_config(page_title="AI Study Management System", layout="centered")

st.title("AI Study Management System")

# Sidebar settings
st.sidebar.header("Model Settings")

MODEL_NAME = st.sidebar.selectbox(
    "Select Model",
    ["gpt-4o-mini"]
)

TEMPERATURE = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.3
)

MAX_TOKENS = st.sidebar.slider(
    "Max Tokens",
    min_value=100,
    max_value=2000,
    value=800
)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to generate AI responses
def generate_response(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content

# Tabs for features
tab1, tab2, tab3, tab4 = st.tabs(
    ["Notes Summarization", "Flashcard Generation", "Quiz Generation", "Answer Evaluation"]
)

# Shared input text
study_text = st.text_area(
    "Enter your study text",
    height=200
)

# -------------------- Notes Summarization --------------------
with tab1:
    if st.button("Generate Summary"):
        if study_text.strip():
            with st.spinner("Generating summary..."):
                result = generate_response(
                    f"""
Summarize the following study notes clearly and concisely while preserving key concepts.

Text:
{study_text}
"""
                )
                st.success(result)

# -------------------- Flashcard Generation --------------------
with tab2:
    if st.button("Generate Flashcards"):
        if study_text.strip():
            with st.spinner("Generating flashcards..."):
                result = generate_response(
                    f"""
Generate question–answer flashcards from the following text.
Return the output in a clear and readable format.

Text:
{study_text}
"""
                )
                st.success(result)

# -------------------- Quiz Generation --------------------
with tab3:
    if st.button("Generate Quiz"):
        if study_text.strip():
            with st.spinner("Generating quiz questions..."):
                result = generate_response(
                    f"""
Generate multiple-choice questions from the following text.
Each question must include four options and clearly indicate the correct answer.

Text:
{study_text}
"""
                )
                st.success(result)

# -------------------- Answer Evaluation --------------------
with tab4:
    correct_answer = st.text_area(
        "Correct Answer",
        height=120
    )

    user_answer = st.text_area(
        "User Answer",
        height=120
    )

    if st.button("Evaluate Answer"):
        if correct_answer.strip() and user_answer.strip():
            with st.spinner("Evaluating answer..."):
                result = generate_response(
                    f"""
Evaluate the user's answer by comparing it with the correct answer.

Correct Answer:
{correct_answer}

User Answer:
{user_answer}

Return the evaluation strictly in JSON format:
{{
  "score": 0-100,
  "feedback": "brief and clear feedback"
}}
"""
                )
                st.success(result)
