from src.llm.gemini_client import generate_response

response = generate_response(
    "Explain SQL in one sentence , Explain in 10 bullet points."
)

print(response)