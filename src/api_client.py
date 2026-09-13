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
  """
  Sends a message to the AI API and returns the response.
  """

  response = client.chat(
      model = "command-a-03-2025",
      messages = messages
  )

  return response