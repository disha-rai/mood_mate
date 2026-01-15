import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="moodmate_db"
        )
        return connection
    except mysql.connector.error as err:
        print("database connection failed:", err)
        return None
    
def save_conversation(user_)