from src.database.crud import (
    save_ai_conversation,
    get_ai_conversation_history
)

conversation = save_ai_conversation(
    user_id=1,
    question="How can I become a Data Scientist?",
    response="Learn Python, SQL, Machine Learning..."
)

print(conversation.id)

history = get_ai_conversation_history(1)

for chat in history:
    print(chat.question)
    print(chat.response)
    print("-" * 50)