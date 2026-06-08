from google import genai
from src.llm.gemini_client import client
import time


def ask_career_ai(question):

    prompt = f"""
    You are an expert career coach.

    Help users with:
    - Career guidance
    - Interview preparation
    - Project ideas
    - Skill development
    - Learning roadmaps

    User Question:
    {question}
    """

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"Attempt {attempt+1}: {e}")

            time.sleep(2)

    return (
        "AI service is temporarily unavailable. "
        "Please try again later."
    )