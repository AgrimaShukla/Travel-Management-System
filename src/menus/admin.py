'''This module displays the admin operations'''

from src.config.prompt import PrintPrompts, InputPrompts
from src.controllers.admin_controller.package_module import Package
from src.controllers.admin_controller.itinerary_module import Itinerary
from src.config.queries import Query

def admin_menu() -> None:
    '''Function to show the admin menu'''
    while True:
        print(PrintPrompts.ADMIN_MENU)
        parameter = input(InputPrompts.ENTER)
        match parameter:
            case '1': Package()
            case '2': Package.change_status_package('inactive')
            case '3': Package.change_status_package('active')
            case '4': Package.show_package(Query.SELECT_PACKAGE, None)
            case '5': Package.update_in_package()
            case '6': 
                while True:
                    print(PrintPrompts.ITINERARY_MENU)
                    parameter = input(InputPrompts.ENTER)
                    match parameter:
                        case '1': 
                                while True:
                                    package_id = input(InputPrompts.PACKAGE_ID)
                                    data = Package.check_package((package_id, ))
                                    if not data:
                                        print(PrintPrompts.PACKAGE_NOT_FOUND)
                                    else:    
                                        Itinerary(package_id)
                                        break
                        case '2': Itinerary.show_itinerary()
                        case '3': Itinerary.update_in_itinerary()
                        case '4': break
                        case _: print(PrintPrompts.INVALID_PROMPT)
            case '7': break
            case _: print(PrintPrompts.INVALID_PROMPT)
