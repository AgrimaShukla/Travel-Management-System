import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv


# dotenv_path = Path('.env')
# load_dotenv(dotenv_path=dotenv_path)
load_dotenv()
class DatabaseConnection:

    MYSQL_USER = "avnadmin"
    MYSQL_PASSWORD = "AVNS_qBnt5Jrh8c06ES1eh7X"
    MYSQL_HOST = "mysql-8b6dd5e-shuklafeb02-24c1.a.aivencloud.com"
    MYSQL_DB = "TravelManagementSystem"
    MYSQL_PORT = 23195

    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        self.setup_connection()

    def setup_connection(self):
        try:
            timeout = 10
            self.connection = pymysql.connect(
                charset="utf8mb4",
                connect_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
                db="TravelManagementSystem",
                host=DatabaseConnection.MYSQL_HOST,
                password=DatabaseConnection.MYSQL_PASSWORD,
                read_timeout=timeout,
                port=DatabaseConnection.MYSQL_PORT,
                user=DatabaseConnection.MYSQL_USER,
                write_timeout=timeout
            )
            
            self.cursor = self.connection.cursor()
            # self.cursor.execute(InitializeDatabase.CREATE_DATABASE.format(DatabaseConnection.MYSQL_DB))
            # self.cursor.execute(InitializeDatabase.USE_DATABASE.format(DatabaseConnection.MYSQL_DB))
            self.connection =self.connection
            self.cursor = self.cursor
        except pymysql.Error as e:
            raise pymysql.Error from e
        
    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()