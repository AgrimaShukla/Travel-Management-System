'''This module displays the admin operations'''

from config.prompt import PrintPrompts, InputPrompts
from view.admin_view.package_module import Package
from view.admin_view.itinerary_module import Itinerary
from controller.admin_controller.package import PackageController

from config.queries import Query


class AdminMenu:
    '''Displaying admin menu'''

    def __init__(self) -> None:
        self.obj_package = Package()
        self.obj_itinerary = Itinerary()
        self.package_cont = PackageController()

    def admin_menu(self) -> None:
        '''Function to show the admin menu'''
        while True:
            print(PrintPrompts.ADMIN_MENU)
            parameter = input(InputPrompts.ENTER)
            match parameter:
                case '1': self.obj_package.add_package()
                case '2': self.obj_package.change_status_package('inactive')
                case '3': self.obj_package.change_status_package('active')
                case '4': self.obj_package.show_package(Query.SELECT_PACKAGE, None)
                case '5': self.obj_package.update_package()
                case '6': 
                    while True:
                        print(PrintPrompts.ITINERARY_MENU)
                        parameter = input(InputPrompts.ENTER)
                        match parameter:
                            case '1': 
                                    while True:
                                        package_id = input(InputPrompts.PACKAGE_ID)
                                        data = self.package_cont.check_package((package_id, ))
                                        if not data:
                                            print(PrintPrompts.PACKAGE_NOT_FOUND)
                                        else:  
                                            self.obj_itinerary.add_itinerary(package_id)
                                            break
                            case '2': self.obj_itinerary.show_itinerary()
                            case '3': self.obj_itinerary.update_itinerary()
                            case '4': break
                            case _: print(PrintPrompts.INVALID_PROMPT)
                case '7': break
                case _: print(PrintPrompts.INVALID_PROMPT)
