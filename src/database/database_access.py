''' This module exceute queries to add, delete, fetch and update the tables'''

import logging
import sqlite3

from src.config.prompt import PrintPrompts
from src.config.queries import Query, DatabaseConfig
from src.database.context_manager import DatabaseConnection

logger = logging.getLogger(__name__)

def insert_table(table_1: str, data_table1: tuple, table_2: str, data_table2: tuple) -> None:
    '''Inserting customer data into database'''
    try:
        with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(table_1, data_table1)
            cursor.execute(Query.ENABLE_FOREIGN_KEY)
            cursor.execute(table_2, data_table2)
            return True
    except sqlite3.IntegrityError as er:
        logger.exception(er)
        print(PrintPrompts.USER_EXISTS)
    except sqlite3.OperationalError as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)
    except sqlite3.Error as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)

def returning_query(query_to_show: str, params = None) -> list:
    '''This function will execute returning queries and return multiple rows'''
    try:
        with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
            cursor = connection.cursor()
            if params:
                cursor = connection.cursor()
                data = cursor.execute(query_to_show, params).fetchall()
                return data
            data = cursor.execute(query_to_show).fetchall()
            return data
    except sqlite3.OperationalError as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)
    except sqlite3.Error as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)

def non_returning_query(query_update: str, params: tuple, prompts: str) -> None:
    '''This function will execute non returning queries'''
    try:
        with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(query_update, params)
            print(prompts)
    except sqlite3.IntegrityError as er:
        logger.exception(er)
        print(PrintPrompts.USER_EXISTS)
    except sqlite3.OperationalError as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)
    except sqlite3.Error as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)

def single_data_returning_query(query_to_check: str, params: tuple) -> tuple:
    '''This function will returning queries and return single row'''
    try:
        with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
            cursor = connection.cursor()
            data = cursor.execute(query_to_check, params).fetchone()
            return data
    except sqlite3.OperationalError as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)
    except sqlite3.Error as er:
        logger.exception(er)
        print(PrintPrompts.UNEXPECTED_ISSUE)
            