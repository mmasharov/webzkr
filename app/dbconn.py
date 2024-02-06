"""Модуль взаимодействия с базой данных"""
import sqlite3
import os

class MyConnectionError(Exception):
    pass

class MyCredentialsError(Exception):
    pass

class MySQLError(Exception):
    pass

class UseMyDatabase:
    """Database use class"""
    def __init__(self, db_path):
        self.db_path = os.path.join(os.getcwd(), db_path)

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            return self.cursor
        except sqlite3.InterfaceError as err:
            raise MyConnectionError(err)
        except sqlite3.ProgrammingError as err:
            raise MyCredentialsError(err)
        
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        if exc_type is sqlite3.ProgrammingError:
            raise MySQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)