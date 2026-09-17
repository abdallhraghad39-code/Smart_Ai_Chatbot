# 🤖 Smart AI Chatbot

A Python-based conversational AI chatbot that integrates with the **Cohere API** to generate intelligent responses to user messages.

The project follows a modular structure, separating API integration, prompt management, conversation handling, and utility functions to keep the code organized, secure, and easy to maintain.

---

## 📌 Project Overview

The **Smart AI Chatbot** allows users to interact with a Cohere language model through a simple command-line interface.

The chatbot is designed to:

- Send user messages to the Cohere API.
- Generate and display AI-powered responses.
- Maintain conversation history for contextual interactions.
- Use structured prompts to guide chatbot behavior.
- Validate user input.
- Handle API and runtime errors gracefully.
- Protect sensitive API credentials using environment variables.
- Support automated testing without exposing or consuming the real API key.

---

## ✨ Features

- 🤖 **Cohere API Integration** — Connects the application to Cohere's language models.
- 💬 **Interactive Chat Loop** — Supports continuous conversations until the user chooses to exit.
- 🧠 **Conversation History** — Maintains previous messages to preserve context.
- 📝 **Structured Prompting** — Uses a system prompt to define chatbot behavior.
- 🔐 **Secure API Key Management** — Stores credentials in a local `.env` file.
- ⚠️ **Error Handling** — Handles invalid input and API-related failures.
- 🔄 **Retry Support** — Provides retry functionality for temporary failures.
- 🧪 **Automated Testing** — Uses mocked API calls so tests can run without a real Cohere request.
- 🧩 **Modular Design** — Separates responsibilities across multiple Python modules.

---

## 🏗️ Project Structure

```text
smart-ai-chatbot/
│
├── src/
│   ├── api_client.py      # Cohere API integration (Member 1)
│   ├── prompts.py         # System prompt & conversation history (Member 2)
│   ├── chatbot.py         # Main conversation loop (Member 3)
│   └── utils.py           # Validation, logging & retry helpers (Member 4)
│
├── tests/
│   └── test_project.py    # Full test suite (Member 4)
│
├── main.py                # Application entry point (Member 4)
├── requirements.txt       # Project dependencies
├── .env.example           # Example environment variables
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

---

## 👥 Team Responsibilities

| Member | Responsibility | Main File |
|---|---|---|
| **Member 1** | Cohere API Integration & API Security | `src/api_client.py` |
| **Member 2** | Prompt Engineering & Conversation History | `src/prompts.py` |
| **Member 3** | Chatbot Logic & Conversation Loop | `src/chatbot.py` |
| **Member 4** | Validation, Error Handling, Testing & Entry Point | `src/utils.py`, `tests/test_project.py`, `main.py` |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd smart-ai-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the API Key

Create a `.env` file in the project root. You can use `.env.example` as a template:

```env
COHERE_API_KEY=your-real-key-here
```

> **Security Note:** Never commit your real `.env` file or API key to GitHub.  
> The `.env` file is excluded through `.gitignore`.

---

## 🚀 Running the Chatbot

Start the application with:

```bash
python main.py
```

Then enter a message when prompted.

Example:

```text
You: Explain machine learning simply.

AI: Machine learning is a way for computers to learn patterns from data
and use those patterns to make predictions or decisions.

You: exit
```

Type `exit` to end the conversation.

---

## 🧪 Running the Tests

Run the complete test suite using:

```bash
python -m unittest discover -s tests -v
```

The tests use a **mocked Cohere client**, meaning:

- No real API request is sent.
- No real API key is required.
- Tests can run quickly and safely without consuming API usage.

---

## 🔐 Security

The project follows basic API security practices:

- API keys are stored using environment variables.
- `.env` is excluded from Git tracking.
- `.env.example` contains only placeholder values.
- Sensitive credentials are never hardcoded in the Python source code.

---

## 🔄 Application Flow

```text
User Input
    ↓
Input Validation
    ↓
Conversation History + System Prompt
    ↓
Cohere API Request
    ↓
AI Response
    ↓
Display Response
    ↓
Continue Conversation / Exit
```

---

## 🛠️ Technologies Used

- **Python**
- **Cohere API**
- **python-dotenv**
- **Git & GitHub**
- **unittest**
- **Mocking for API Testing**

---

## 📚 Key Concepts Demonstrated

This project demonstrates practical experience with:

- API Integration
- Prompt Engineering
- Environment Variables
- Secure API Key Management
- Modular Python Programming
- Conversation State Management
- Error Handling
- Automated Testing
- Git/GitHub Collaboration
