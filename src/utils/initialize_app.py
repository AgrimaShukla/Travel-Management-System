'''This module is for creating all tables and adding an admin'''

import shortuuid
import hashlib
import logging
import os 
from os.path import join, dirname
from config.queries import Query
from dotenv import load_dotenv
from database.database_access import QueryExecutor
from utils.exception import exception_handler

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = logging.getLogger(__name__)

@exception_handler
def create_admin() -> None:
    '''To add admin in the table if non present'''
    obj_query_executor = QueryExecutor()
    obj_query_executor.create_tables()
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    NAME = os.getenv('NAME')
    MOBILE_NUMBER = os.getenv('MOBILE_NUMBER')
    GENDER = os.getenv('GENDER')
    AGE = os.getenv('AGE')
    EMAIL = os.getenv('EMAIL')

    if_admin_exists = obj_query_executor.single_data_returning_query(Query.SELECT_ADMIN, ('admin', ))
    if if_admin_exists == None:
        user_id = 'A_' + shortuuid.ShortUUID().random(length = 8)
        password = hashlib.md5(PASSWORD.encode()).hexdigest()
        admin_credentials = (user_id, USERNAME, password, 'admin')
        admin_info = (user_id, NAME, MOBILE_NUMBER, GENDER, AGE, EMAIL)
        obj_query_executor.insert_table(Query.INSERT_CREDENTIALS, admin_credentials, Query.INSERT_CUSTOMER, admin_info)
       