'''This module is for creating all tables and adding an admin'''

import shortuuid
import hashlib
import sqlite3
import logging
import os 
from os.path import join, dirname

from src.database.context_manager import DatabaseConnection
from src.config.queries import Query, DatabaseConfig
from dotenv import load_dotenv
from src.database import database_access

dotenv_path = join(dirname(__file__), '.env')
print(dotenv_path)
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

    try: 
        with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
            if_admin_exists = database_access.single_data_returning_query(Query.SELECT_ADMIN, ('admin', ))
            if len(if_admin_exists) != 0:
                cursor = connection.cursor()
                user_id = 'A_' + shortuuid.ShortUUID().random(length = 8)
                password = hashlib.md5(PASSWORD.encode()).hexdigest()
                admin_credentials = (user_id, USERNAME, password, 'admin')
                admin_info = (user_id, NAME, MOBILE_NUMBER, GENDER, AGE, EMAIL)
                cursor.execute(Query.INSERT_CREDENTIALS, admin_credentials)
                cursor.execute(Query.INSERT_ADMIN, admin_info)
    except sqlite3.IntegrityError as er:
        logger.exception(er)
    except sqlite3.OperationalError as er:
        logger.exception(er)
    except sqlite3.Error as er:
        logger.exception(er)

def create_tables() -> None:
        '''Creating all tables'''
        try:
             with DatabaseConnection(DatabaseConfig.DB_PATH) as connection:
                cursor = connection.cursor()
                cursor.execute(Query.CREATE_CREDENTIALS)
                cursor.execute(Query.CREATE_ADMIN)
                cursor.execute(Query.CREATE_CUSTOMER)
                cursor.execute(Query.CREATE_PACKAGE)
                cursor.execute(Query.CREATE_ITINERARY)
                cursor.execute(Query.CREATE_BOOKING)
                cursor.execute(Query.CREATE_BOOKING_PACKAGE)
                cursor.execute(Query.CREATE_REVIEW)
        except sqlite3.IntegrityError as er:
            logger.exception(er)
        except sqlite3.OperationalError as er:
            logger.exception(er)
        except sqlite3.Error as er:
            logger.exception(er)
        