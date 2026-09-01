from sqlite3 import connect

def get_db_connection():
    try:
        conn = connect('database.db')
        return True
    except:
        get_db_connection()