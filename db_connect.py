# SQLite is relational DB to be used
from sqlite3 import connect 

# Creating singleton for DB Connection
class DB_connection:
    connection_instance = None

    @staticmethod
    def getConnection():
        if DB_connection.connection_instance == None:
            DB_connection()
        return DB_connection.connection_instance
    
    def __init__(self):
        if DB_connection.connection_instance != None:
            raise Exception("Make sure you're not trying to build multiple instances of this \
                class. Remember this is a singleton!")
        else:
            DB_connection.connection_instance = self
            self.connection = connect("tesBillProject.db")

