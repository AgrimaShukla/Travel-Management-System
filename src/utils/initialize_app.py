'''This module is for creating all tables and adding an admin'''

import shortuuid
import hashlib
import sqlite3
import logging

from src.database.context_manager import DatabaseConnection
from src.config.queries import Query
from src.database import database_access

logger = logging.getLogger(__name__)
def create_admin():
    '''To add admin in the table if non present'''
    with DatabaseConnection('src\\database\\travelmanagementsystem.db') as connection:
        try: 
            if_admin_exists = database_access.single_data_returning_query(Query.SELECT_ADMIN, ('admin', ))
            if len(if_admin_exists) != 0:
                cursor = connection.cursor()
                user_id = 'A_' + shortuuid.ShortUUID().random(length = 8)
                password = hashlib.md5('admin123'.encode()).hexdigest()
                admin_credentials = (user_id, 'admin123', password, 'admin')
                admin_info = (user_id, 'amaira singh', 9087890987, 'female', 34, 'amaira@gmail.com')
                cursor.execute(Query.INSERT_CREDENTIALS, admin_credentials)
                cursor.execute(Query.INSERT_ADMIN, admin_info)
        except sqlite3.IntegrityError as er:
            logger.exception(er)
        except sqlite3.OperationalError as er:
            logger.exception(er)
        except sqlite3.Error as er:
            logger.exception(er)

def create_tables() -> None:
    with DatabaseConnection('src\\database\\travelmanagementsystem.db') as connection:
        '''Creating all tables'''
        cursor = connection.cursor()
        cursor.execute(Query.CREATE_CREDENTIALS)
        cursor.execute(Query.CREATE_ADMIN)
        cursor.execute(Query.CREATE_CUSTOMER)
        cursor.execute(Query.CREATE_PACKAGE)
        cursor.execute(Query.CREATE_ITINERARY)
        cursor.execute(Query.CREATE_BOOKING)
        cursor.execute(Query.CREATE_BOOKING_PACKAGE)
        