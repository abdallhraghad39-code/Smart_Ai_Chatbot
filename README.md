# Smart AI Chatbot — TechMaster Academy, Phase 04 / Project 04

A conversational AI assistant that sends user messages to Cohere's API and
returns responses through a controlled chatbot loop, with structured
prompts, conversation history, and error handling.

## Project structure

```
smart-ai-chatbot/
├── src/
│   ├── api_client.py    # Cohere integration (Member 1)
│   ├── prompts.py       # System prompt + conversation history (Member 2)
│   ├── chatbot.py        # Main conversation loop (Member 3)
│   └── utils.py          # Validation, logging, retry helper (Member 4)
├── tests/
│   └── test_project.py   # Full test suite (Member 4)
├── main.py                # Entry point (Member 4)
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project root (copy `.env.example`):
   ```
   COHERE_API_KEY=your-real-key-here
   ```
   Never commit `.env` — it's already in `.gitignore`.

## Running the chatbot

```
python main.py
```

Type a message and press Enter. Type `exit` to end the conversation.

## Running the tests

```
python -m unittest discover -s tests -v
```

The tests mock the Cohere client, so **no real API key or network call is
needed** to run them — they're fast, free, and safe to run in CI.