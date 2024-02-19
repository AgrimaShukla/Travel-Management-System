import os
from pathlib import Path

import mysql.connector
import pymysql
from dotenv import load_dotenv
from config.queries import InitializeDatabase

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
class DatabaseConnection:

    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_DB = os.getenv('MYSQL_DB')

    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        self.setup_connection()

    def setup_connection(self):

        try:
            timeout = 10
            self.connection = pymysql.connect(
                charset = 'utf8mb4',
                connect_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
                user = DatabaseConnection.MYSQL_USER,
                password = DatabaseConnection.MYSQL_PASSWORD,
                host = DatabaseConnection.MYSQL_HOST,
                read_timeout=timeout,
                write_timeout=timeout
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute(InitializeDatabase.CREATE_DATABASE.format(DatabaseConnection.MYSQL_DB))
            self.cursor.execute(InitializeDatabase.USE_DATABASE.format(DatabaseConnection.MYSQL_DB))
            
        except pymysql.Error as e:
            raise pymysql.Error from e
        
    def __enter__(self) -> mysql.connector.connection.MySQLConnection:
        return self.connection

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        if exc_type or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
            