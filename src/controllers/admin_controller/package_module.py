''' Admin operations are handled in this module.
    - Add package
    - Activate package
    - Deactivate package
    - Update package
 '''
import logging
import shortuuid

from src.config.queries import Query 
from src.utils import validation
from src.database import database_access
from src.config.prompt import PrintPrompts, InputPrompts, LoggingPrompt
from src.config.prompt_values import update_package
from src.utils.pretty_print import data_tabulate
from src.utils.validation import validate
from src.config.regex_value import RegularExp

logger = logging.getLogger(__name__)

class Package:
    '''New Package created'''
    def __init__(self):
        self.package_id = 'P_' + shortuuid.ShortUUID().random(length = 8)
        self.package_name = validate(InputPrompts.INPUT.format('package name'), RegularExp.STRING_VALUE)
        self.duration = validation.validate(InputPrompts.DURATION, RegularExp.DURATION)
        self.category = validate(InputPrompts.INPUT.format('category'), RegularExp.STRING_VALUE)
        self.price = validate(InputPrompts.INPUT.format('price'), RegularExp.NUMBER_VALUE)
        self.lmt = validate(InputPrompts.INPUT.format('limit'), RegularExp.NUMBER_VALUE)
        self.status = validation.validate(InputPrompts.STATUS, RegularExp.STATUS)
        self.add_package()
 

    def add_package(self) -> None:
        '''New package added to database'''
        data = (self.package_id, self.package_name, self.duration, self.category, self.price, self.lmt, self.status)
        database_access.non_returning_query(Query.INSERT_PACKAGE_QUERY, data, PrintPrompts.ADDED)
        logger.info(LoggingPrompt.ADDED_PACKAGE)


    @staticmethod
    def show_package(query_to_execute: str, status: tuple) -> None:
        '''To display packages'''
        data = database_access.returning_query(query_to_execute, status)
        if not data:
            logger.info(LoggingPrompt.NO_PACKAGE)
            return False
        else:
            data_tabulate(data, ["PACKAGE_ID", "PACKAGE_NAME", "DURATION", "CATEGORY", "PRICE", "LIMIT", "STATUS"])
            return True


    @staticmethod
    def check_package(package_data: tuple) -> list:
        '''To check package if it exists or not'''
        data = database_access.single_data_returning_query(Query.CHECK_PACKAGE_QUERY, package_data) 
        return data


    @staticmethod
    def change_status_package(status: str) -> None:
        '''Change status of package'''
        not_exist_package = Package.show_package(Query.SELECT_PACKAGE_QUERY, (status, ))
        if not_exist_package == True:
            package_id = input(InputPrompts.PACKAGE_ID)
            data = Package.check_package((package_id, ))
            if data:
                data = (status, package_id)
                database_access.non_returning_query(Query.CHANGE_STATUS_QUERY, data, PrintPrompts.CHANGED)
            else:
                print(PrintPrompts.NO_PACKAGE.format(package_id))
        else:
            print(PrintPrompts.NO_PACKAGE_FOUND)


    @staticmethod
    def update_in_package() -> None:
        '''Make changes in existing package'''
        not_exist_package = Package.show_package(Query.SELECT_PACKAGE, None)
        # if-else to check if table is empty or not
        if not_exist_package == True:
            while True:
                package_id = input(InputPrompts.PACKAGE_ID)
                # to check if package exists or not
                data = Package.check_package((package_id, ))
                if data:
                    print(PrintPrompts.UPDATE_PACKAGE)
                    value = input(InputPrompts.ENTER)
                    match value:
                        case '1': 
                            updated_value = validate(InputPrompts.INPUT.format('package name'), RegularExp.STRING_VALUE)
                        case '2': 
                            updated_value = validate(InputPrompts.DURATION, RegularExp.DURATION)
                        case '3':
                            updated_value = validate(InputPrompts.INPUT.format('category'), RegularExp.STRING_VALUE)
                        case '4':
                            updated_value = validate(InputPrompts.INPUT.format('price'), RegularExp.NUMBER_VALUE)
                        case '5':
                            updated_value = validate(InputPrompts.INPUT.format('LIMIT'), RegularExp.NUMBER_VALUE)
                        case _: 
                            print(PrintPrompts.INVALID_PROMPT)
                            continue
                    column_name = update_package[value]
                    data = (updated_value, package_id)
                    database_access.non_returning_query(Query.UPDATE_PACKAGE_QUERY.format(column_name), data, PrintPrompts.UPDATED)
                    break
                else:
                    print(PrintPrompts.NO_PACKAGE.format(package_id))
        else:
            print(PrintPrompts.NO_PACKAGE_FOUND)        