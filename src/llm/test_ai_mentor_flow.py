from src.llm.career_chat import ask_career_ai

from src.database.crud import (
    save_ai_conversation,
    get_ai_conversation_history
)

user_id = 1

question = "How can I become a Data Scientist?"

print("Generating AI Response...\n")

response = ask_career_ai(question)

print(response)

save_ai_conversation(
    user_id=user_id,
    question=question,
    response=response
)

print("\nConversation Saved\n")

history = get_ai_conversation_history(user_id)

print("Chat History\n")

for chat in history[:5]:

    print(f"Question: {chat.question}")

    print(f"Response: {chat.response[:100]}...")

    print("-" * 50)