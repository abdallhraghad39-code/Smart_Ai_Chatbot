# src/prompts.py

# 1. Define the System Prompt
SYSTEM_PROMPT = """
You are a helpful, beginner-friendly programming tutor for TechMaster Academy. 
Your task is to answer technical questions clearly. 
Assume the user is a beginner who is just learning Python. 
Keep your explanations under 150 words and use simple analogies. 
Provide your answers in short, readable paragraphs.
"""

def initialize_history():
    """Creates the initial conversation history with the system prompt."""
    history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    return history

def build_prompt(conversation_history, user_text):
    """Appends the user's new message to the history."""
    new_message = {"role": "user", "content": user_text}
    conversation_history.append(new_message)
    return conversation_history

def add_assistant_reply(conversation_history, ai_text):
    """Appends the AI's generated response back into the history."""
    ai_message = {"role": "assistant", "content": ai_text}
    conversation_history.append(ai_message)
    return conversation_history