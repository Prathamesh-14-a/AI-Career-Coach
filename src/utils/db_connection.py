import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="career_coach",
            user="postgres",
            password="Pratham@2006",
            host="localhost",
            port="5432"
        )
        print("Connected successfully to the database.")
        return conn
    except Exception as e:
        print("Connection failed:", e)