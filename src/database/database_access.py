''' This module exceute queries to add, delete, fetch and update the tables'''

import logging
import sqlite3

from config.prompt import PrintPrompts
from config.queries import Query, DatabaseConfig
from database.context_manager import DatabaseConnection

logger = logging.getLogger(__name__)

class QueryExecutor:

    def __init__(self) -> None:
        self.path = DatabaseConfig.DB_PATH

    def insert_table(self, table_1: str, data_table1: tuple, table_2: str, data_table2: tuple) -> None:
        '''Inserting customer data into database'''
        
        with DatabaseConnection(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute(table_1, data_table1)
            cursor.execute(Query.ENABLE_FOREIGN_KEY)
            cursor.execute(table_2, data_table2)
            return True
     
    def returning_query(self, query_to_show: str, params = None) -> list:
        '''This function will execute returning queries and return multiple rows'''
        with DatabaseConnection(self.path) as connection:
            cursor = connection.cursor()
            if params:
                data = cursor.execute(query_to_show, params).fetchall()
                return data
            data = cursor.execute(query_to_show).fetchall()
            return data
       

    def non_returning_query(self, query_update: str, params: tuple) -> None:
        '''This function will execute non returning queries'''
        try:
            with DatabaseConnection(self.path) as connection:
                cursor = connection.cursor()
                cursor.execute(query_update, params)
                return True
        except sqlite3.IntegrityError as er:
            logger.exception(er)
            print(PrintPrompts.USER_EXISTS)
        except sqlite3.Error as er:
            logger.exception(er)
            print(PrintPrompts.UNEXPECTED_ISSUE)

    def single_data_returning_query(self, query_to_check: str, params: tuple) -> tuple:
        '''This function will returning queries and return single row'''
        try:
            with DatabaseConnection(self.path) as connection:
                cursor = connection.cursor()
                data = cursor.execute(query_to_check, params).fetchone()
                return data
        except sqlite3.Error as er:
            logger.exception(er)
            print(PrintPrompts.UNEXPECTED_ISSUE)

    def create_tables(self) -> None:
        '''Creating all tables'''
        try:
            with DatabaseConnection(self.path) as connection:
                cursor = connection.cursor()
                cursor.execute(Query.CREATE_CREDENTIALS)
                cursor.execute(Query.CREATE_ADMIN)
                cursor.execute(Query.CREATE_CUSTOMER)
                cursor.execute(Query.CREATE_PACKAGE)
                cursor.execute(Query.CREATE_ITINERARY)
                cursor.execute(Query.CREATE_BOOKING)
                cursor.execute(Query.CREATE_BOOKING_PACKAGE)
                cursor.execute(Query.CREATE_REVIEW)
        except sqlite3.Error as er:
            logger.exception(er)            