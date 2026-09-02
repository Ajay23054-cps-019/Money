from sqlite3 import connect

class database:
    def __init__():
        try:
            conn = connect('database.db')
            self.conn = conn
            self.add_data()
            return True
        except:
            self.__init__()

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
        conn.close()