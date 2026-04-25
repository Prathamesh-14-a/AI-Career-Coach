print("AI Career Coach Project Started...")

from src.utils.db_connection import get_connection

conn = get_connection()
print(conn)
