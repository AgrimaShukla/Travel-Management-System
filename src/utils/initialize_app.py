'''This module is for creating all tables and adding an admin'''

import shortuuid
import hashlib
import mysql.connector
import logging
import os 
from os.path import join, dirname

from database.context_manager import DatabaseConnection
from config.queries import Query, DatabaseConfig
from dotenv import load_dotenv
from database.database_access import QueryExecutor

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = logging.getLogger(__name__)
def create_admin() -> None:
    '''To add admin in the table if non present'''

    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    NAME = os.getenv('NAME')
    MOBILE_NUMBER = os.getenv('MOBILE_NUMBER')
    GENDER = os.getenv('GENDER')
    AGE = os.getenv('AGE')
    EMAIL = os.getenv('EMAIL')
    # print(type(USERNAME), type(PASSWORD), type(NAME), type(MOBILE_NUMBER), type(GENDER), type(AGE), type(EMAIL))
    obj_query_executor = QueryExecutor()
    if_admin_exists = obj_query_executor.single_data_returning_query(Query.SELECT_ADMIN, ('admin', ))
    if if_admin_exists == None:
        user_id = 'A_' + shortuuid.ShortUUID().random(length = 8)
        password = hashlib.md5(PASSWORD.encode()).hexdigest()
        admin_credentials = (user_id, USERNAME, password, 'admin')
        admin_info = (user_id, NAME, MOBILE_NUMBER, GENDER, AGE, EMAIL)
        obj_query_executor.insert_table(Query.INSERT_CREDENTIALS, admin_credentials, Query.INSERT_USER, admin_info)
        
   
def create_tables() -> None:
        '''Creating all tables'''
        try:
            with DatabaseConnection() as connection:
                cursor = connection.cursor()
                cursor.execute(Query.CREATE_CREDENTIALS)
                cursor.execute(Query.CREATE_CUSTOMER)
                cursor.execute(Query.CREATE_PACKAGE)
                cursor.execute(Query.CREATE_ITINERARY)
                cursor.execute(Query.CREATE_BOOKING)
                cursor.execute(Query.CREATE_BOOKING_PACKAGE)
                cursor.execute(Query.CREATE_REVIEW)
        except pymysql.Error as er:
            logger.exception(er)
        