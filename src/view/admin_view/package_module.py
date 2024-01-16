''' Admin operations are handled in this module.
    - Add package
    - Activate package
    - Deactivate package
    - Update package
 '''
import logging

from config.queries import Query 
from config.prompt import PrintPrompts, InputPrompts, LoggingPrompt, TabulateHeader
from utils.pretty_print import data_tabulate
from utils.validation import validate, validate_uuid

from config.regex_value import RegularExp
from controller.admin_controller.package import PackageController

logger = logging.getLogger(__name__)   

class Package:
    '''New Package created'''
    def __init__(self) -> None:
        self.pack_controller = PackageController()

    def add_package(self) -> None:
        '''New package added to database'''
        while True:
            package_name = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('package name'))
            duration = validate(RegularExp.DURATION, InputPrompts.DURATION)
            category = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('category'))
            price = validate(RegularExp.NUMBER_VALUE, InputPrompts.INPUT.format('price'))
            status = validate(RegularExp.STATUS, InputPrompts.STATUS)
            inserted = self.pack_controller.add_package(package_name, duration, category, price, status)
            logger.info(LoggingPrompt.ADDED_PACKAGE)
            if inserted == True:
                print(PrintPrompts.INSERTED)
                break
            else:
                print(PrintPrompts.UNEXPECTED_ISSUE)

    def show_package(self, query_to_execute: str, status: tuple) -> bool:
        '''To display packages'''
        data = self.pack_controller.fetch_package(query_to_execute, status)
        if not data:
            logger.info(LoggingPrompt.NO_PACKAGE)
            return False
        else:
            data_tabulate(data, (TabulateHeader.PACKAGE_ID, TabulateHeader.PACKAGE_NAME, TabulateHeader.DURATION, TabulateHeader.CATEGORY, TabulateHeader.PRICE, TabulateHeader.STATUS))
            return True


    def change_status_package(self, status: str) -> None:
        '''Change status of package'''
        not_exist_package = self.show_package(Query.SELECT_PACKAGE_QUERY, (status, ))
        while True:
            if not_exist_package == False:
                print(PrintPrompts.NO_PACKAGE_FOUND)
                continue
            package_id = validate_uuid(InputPrompts.PACKAGE_ID, RegularExp.UUID)
            return_value = self.pack_controller.check_package((package_id, ))
            if not return_value:
                print(PrintPrompts.NO_PACKAGE.format(package_id))
                continue
            if_changed = self.pack_controller.change_status_package((status, package_id))
            if if_changed == True:
                print(PrintPrompts.UPDATED)
                break
            else:
                print(PrintPrompts.UNEXPECTED_ISSUE)
        

    def update_package(self):
        not_exist_package = self.show_package(Query.SELECT_PACKAGE, None)
        if not_exist_package == False:
            print(PrintPrompts.NO_PACKAGE_FOUND)
        while True:
            package_id = validate_uuid(InputPrompts.PACKAGE_ID, RegularExp.UUID)
            return_value = self.pack_controller.check_package((package_id, ))
            if not return_value:
                print(PrintPrompts.NO_PACKAGE.format(package_id))
                continue
            print(PrintPrompts.UPDATE_PACKAGE)
            value = input(InputPrompts.ENTER)  
            match value:
                case '1': 
                    updated_value = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('package name'))
                case '2':
                    updated_value = validate(RegularExp.DURATION, InputPrompts.INPUT.format('duration'))
                case '3':
                    updated_value = validate(RegularExp.STRING_VALUE, InputPrompts.INPUT.format('category'))
                case '4':
                    updated_value = validate(RegularExp.NUMBER_VALUE , InputPrompts.INPUT.format('price'))
                case _: 
                    print(PrintPrompts.INVALID_PROMPT)
                    continue

            return_value = self.pack_controller.update_in_package(package_id, value, updated_value)
            if return_value == -1:
                print(PrintPrompts.NO_PACKAGE.format(package_id))
            elif return_value == True:
                print(PrintPrompts.UPDATED)
                break
            else:
                print(PrintPrompts.UNEXPECTED_ISSUE)