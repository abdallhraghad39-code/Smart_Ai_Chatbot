import os
import cohere
from dotenv import load_dotenv

#LOAD VARIABLES FROM .ENV
load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")

#CHECK IF API KEY EXISTS
if not API_KEY:
  raise ValueError("COHERE_API_KEY is not set")

#INITIALIZE COHERE CLIENT
client = cohere.ClientV2(API_KEY)

# =====================================
# Send Request to AI API
# =====================================

def get_ai_response(messages):

    try:

        response = client.chat(

            model="command-a-03-2025",

            messages=messages,

            temperature=0.5

        )

        text = response.message.content[0].text

        return text.strip()

    except Exception as error:

        print(f"API Error: {error}")

        return (

            "Sorry, something went wrong while contacting the AI service. "

            "Please try again."

        )