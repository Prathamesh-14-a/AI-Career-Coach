from src.database.crud import create_user

user = create_user(
    username="Pratham",
    email="pratham@gmail.com",
    password_hash="test123"
)

print('User Created')