import sqlite3
from sqlite3 import Connection

class DatabaseConnection:

    def __init__(self, host: str) -> None:
        self.connection = None
        self.host = host

    def __enter__(self) -> Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        if exc_type or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
            