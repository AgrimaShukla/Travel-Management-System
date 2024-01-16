''' Travel Itinerary system
    This module is entry point
'''
import logging

from config.prompt import PrintPrompts, InputPrompts 
from view.menus.admin import AdminMenu
from view.menus.user import UserMenu
from view.registration import RegistrationViews
from view.authentication import Authentication
import utils.initialize_app as initialize_app

logging.basicConfig(format = '%(asctime)s - %(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    filename = 'logs.txt',
                    level = logging.DEBUG)

logging.getLogger(__name__)

def main() -> None:
    '''Main function to check if user or admin and show corresponding menu'''
    while True:
        print(PrintPrompts.NAME)
        print(PrintPrompts.ENTRY)
        parameter = input(InputPrompts.ENTER)
        match parameter:
            case '1':
                obj_register = RegistrationViews()
                obj_register.enter_customer_details()
            case '2':
                obj_authenticate = Authentication()
                role = obj_authenticate.user_authentication()
                if role is not None and role[0] == 'user':
                    obj_user = UserMenu(role[1])
                    obj_user.user_menu()
                elif role is not None and role[0] == 'admin':
                    obj_admin = AdminMenu()
                    obj_admin.admin_menu()
            case '3': break
            case _: print(PrintPrompts.INVALID_PROMPT)

if __name__ == "__main__":

    # all the tables will be created
    # initialize_app.create_tables()
    # initialize_app.create_admin()
    main()
