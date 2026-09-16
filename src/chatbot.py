from api_client import get_ai_response
from prompts import build_prompt, update_history

def get_user_input():
    return input("You: ").strip()

def display_response(text):
    print(f"Bot: {text}\n")

def run_chatbot():
    print("Welcome to the AI Chatbot! Type 'exit' to quit.\n")
    
    while True:
        user_msg = get_user_input()
        
        if user_msg.lower() == 'exit':
            print("Ending conversation. Goodbye!")
            break
            
        if not user_msg:
            print("Message cannot be empty. Please try again.")
            continue
            
        prompt_data = build_prompt(user_msg)
        response_text = get_ai_response(prompt_data)
        display_response(response_text)
        update_history(user_msg, response_text)

if __name__ == "__main__":
    run_chatbot()