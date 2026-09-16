import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from utils import logger

try:
    from chatbot import run_chatbot
except ValueError as config_error:
    print(f"Configuration error: {config_error}")
    print("Create a .env file in the project root with:")
    print("    COHERE_API_KEY=your-key-here")
    print("See .env.example for the expected format.")
    sys.exit(1)
except ImportError as import_error:
    # Catches integration bugs
    print(f"Startup error: could not load the chatbot ({import_error}).")
    print("This usually means src/chatbot.py or src/prompts.py has an "
          "import mismatch — check that every function chatbot.py "
          "imports actually exists in prompts.py.")
    sys.exit(1)


def main():
    try:
        run_chatbot()
    except KeyboardInterrupt:
        print("\nChatbot interrupted by user. Goodbye!")
    except Exception as e:
        logger.error("Unexpected fatal error: %s", e)
        print("A fatal error occurred and the chatbot had to stop. "
              "Please try running it again.")


if __name__ == "__main__":
    main()
