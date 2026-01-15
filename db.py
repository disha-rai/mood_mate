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
    

def save_conversation(user_text, emotion, intent, response):
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO conversation_logs (user_text, emotion, intent, response)
        VALUES (%s, %s, %s, %s)
        """
        values = (user_text, emotion, intent, response)
        cursor.execute(query, values)
        connection.commit()
    except Exception as e:
        print("Failed to save conversation:", e)
    finally:
        cursor.close()
        connection.close()
