from sqlite3 import connect

class database:
    def __init__():
        try:
            conn = connect('database.db')
            return True
        except:
            self.__init__()