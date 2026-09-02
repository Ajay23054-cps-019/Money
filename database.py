from sqlite3 import connect

class database:
    def __init__(self):
        try:
            self.conn = connect('database.db')
            self.add_data()
        except Exception:
            self.conn = None

    def add_data(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                name TEXT NOT NULL,
                value TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def __del__(self):
        if getattr(self, "conn", None):
            self.conn.close()