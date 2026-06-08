import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)


def generate_response(prompt: str):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    
    except Exception as e:

        print(f"Gemini Error: {e}")

        return (
            "AI service is temporarily unavailable. "
            "Please try again in a few minutes."
        )
