# Study-Management
Live Application

🔗 Streamlit App:
https://study-management-vn2llevhkjdocsugt5cz2c.streamlit.app/

GitHub Repository

🔗 Source Code:
https://github.com/Ferdaus71/Study-Management

Core AI Features
1️⃣ Flashcard Generation

Automatically generates question–answer pairs

Helps in active recall and memorization

Output is clear, concise, and learner-friendly
Example Input
Machine learning enables systems to learn from data without explicit programming.
Example Output
[
  {
    "question": "What is machine learning?",
    "answer": "Machine learning is a technique that allows systems to learn from data without explicit programming."
  }
]

2️⃣ Quiz Generation

Generates multiple-choice questions (MCQs)

Each question includes multiple options

Clearly identifies the correct answer

Example Output
[
  {
    "question": "What does machine learning allow systems to do?",
    "options": ["Store data", "Learn from data", "Write code", "Design hardware"],
    "correct_answer": "Learn from data"
  }
]

3️⃣ Notes Summarization

Converts long study notes into short, meaningful summaries

Preserves key concepts

Ideal for revision and quick learning

Example Output

Machine learning is a branch of artificial intelligence that enables systems to learn patterns from data and improve performance over time.

4️⃣ (Optional) Answer Evaluation

Evaluates user answers against correct answers

Provides:

📊 Score (0–100)

📝 Brief feedback

Example Output
{
  "score": 85,
  "feedback": "Good understanding, but the explanation can be more precise."
}

Prompt Engineering Approach

Separate prompts for:

Flashcards

Quizzes

Summaries

Answer evaluation

Prompts are designed to:

Ensure structured outputs

Maintain consistency

Reduce hallucinations

JSON-based outputs for easy parsing

System Architecture
User Input
   ↓
Streamlit UI
   ↓
Prompt Layer
   ↓
OpenAI LLM (GPT)
   ↓
Structured Educational Output

Tech Stack

Frontend: Streamlit

Backend: Python

AI Model: OpenAI GPT (e.g., gpt-4o-mini)

Deployment: Streamlit Cloud

Version Control: GitHub

Project Structure
Study-Management/
│
├── app.py               # Streamlit application
├── requirements.txt     # Dependencies
├── README.md            # Project documentation

Setup Instructions (Local)
1️⃣ Clone the Repository
git clone https://github.com/Ferdaus71/Study-Management.git
cd Study-Management

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Environment Variable

Create a .env file:
OPENAI_API_KEY=your_openai_api_key_here

4️⃣ Run the App
streamlit run app.py

Deployment (Streamlit Cloud)

Push code to GitHub

Go to https://streamlit.io/cloud

Create a new app

Select repository & app.py

Add Secrets:
OPENAI_API_KEY = "your_openai_api_key_here"
Than Deploy 🚀

Evaluation Criteria Mapping
| Criteria                 | How It Is Addressed                        |
| ------------------------ | ------------------------------------------ |
| AI system design quality | Modular prompt & engine-based architecture |
| Prompt engineering       | Structured, task-specific prompts          |
| Output accuracy          | Controlled temperature & JSON formatting   |
| Code clarity             | Clean, readable Python code                |
| Documentation            | Detailed README with examples              |
| Deployment               | Live Streamlit app with GitHub link        |


👨‍🎓 Author

Md. Ferdaus Hossen
B.Sc. in Computer Science & Engineering
Green University of Bangladesh

📌 Future Improvements

PDF upload support

User authentication

Score analytics dashboard

Multilingual (Bangla + English)

Fine-tuned educational model
