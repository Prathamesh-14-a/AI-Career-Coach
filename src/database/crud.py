from src.database.db_connection import SessionLocal
from src.database.models import User


#-------------------------------------------------------
# CREATE USER FUNCTION
#-------------------------------------------------------
def create_user(username , email , password_hash):

    session = SessionLocal()

    try:
        user = User(
            username = username , 
            email = email ,
            password_hash = password_hash
        )

        session.add(user)
        session.commit()

        return user

    finally:
        session.close()