''' Travel Itinerary system
    This module is entry point
'''
import logging
import sys

from src.config.prompt import PrintPrompts, InputPrompts 
from src.menus import user, admin
from src.controllers.registration import Registration
from src.utils.authentication import Authentication
from src.utils import initialize_app


logging.basicConfig(format = '%(asctime)s - %(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    filename = 'logs.txt',
                    level = logging.DEBUG)

logging.getLogger(__name__)

def main() -> None:
    '''Main function to check if user or admin and show corresponding menu'''
    while True:
        print(PrintPrompts.NAME)
        print(PrintPrompts.LOGIN_ATTEMPTS)
        print(PrintPrompts.ENTRY)
        parameter = input(InputPrompts.ENTER)
        match parameter:
            case '1':
                Registration()
                continue
            case '2':
                obj_authenticate = Authentication()
                role = obj_authenticate.user_authentication()
                if role is not None and role[0] == 'user':
                    user.user_menu(role[1])
                elif role is not None and role[0] == 'admin':
                    admin.admin_menu()
                else:
                    continue
            case _: print(PrintPrompts.INVALID_PROMPT)

if __name__ == "__main__":

    # all the tables will be created
    initialize_app.create_tables()
    # initialize_app.create_admin()
    main()

else:
    sys.exit()