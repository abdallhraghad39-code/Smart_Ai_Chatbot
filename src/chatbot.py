from api_client import get_ai_response
from prompts import initialize_history, build_prompt, add_assistant_reply

def get_user_input():
    return input("You: ").strip()

def display_response(text):
    print(f"Bot: {text}\n")

def run_chatbot():
    print("Welcome to the AI Chatbot! Type 'exit' to quit.\n")
    conversation_history = initialize_history() 

    while True:
        user_msg = get_user_input()
        
        if user_msg.lower() == 'exit':
            print("Ending conversation. Goodbye!")
            break
            
        if not user_msg:
            print("Message cannot be empty. Please try again.")
            continue
            
        conversation_history = build_prompt(conversation_history, user_msg)
        response_text = get_ai_response(conversation_history)
        display_response(response_text)
        conversation_history = add_assistant_reply(conversation_history, response_text)

if __name__ == "__main__":
    run_chatbot()