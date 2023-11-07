'''This module handles user preference for the packages'''

from src.config.prompt import PrintPrompts, InputPrompts
from src.controllers.customer_controller import view_package, BookPackage

def day_menu(dest_option: str, category_option: str, customer_id: str) -> None:
    '''User can choose days'''
    while True:
        print(PrintPrompts.DAY_PROMPT)
        option = input(InputPrompts.ENTER)
        if option in ['1', '2', '3']:
            view_package(dest_option, category_option, option, customer_id)
        elif option == '4':
            break
        else:
            print(PrintPrompts.INVALID_PROMPT)

def category_menu(dest_option: str, customer_id: str) -> None:
    '''User can choose category'''
    while True:
        print(PrintPrompts.CATEGORY_PROMPT)
        option = input(InputPrompts.ENTER)
        if option in ['1', '2', '3']:
            day_menu(dest_option, option, customer_id)
        elif option == '4':
            break
        else:
            print(PrintPrompts.INVALID_PROMPT)

def destination_menu(customer_id: str) -> None:
    '''User can choose destination'''
    while True:
        print(PrintPrompts.DESTINATION_PROMPT)
        option = input(InputPrompts.ENTER)
        if option in ['1', '2', '3', '4', '5']:
            category_menu(option, customer_id)
        elif option == '6':
            break
        else:
            print(PrintPrompts.INVALID_PROMPT)

def user_menu(customer_id: str) -> None:
    '''To show the user menu'''
    while True:
        print(PrintPrompts.USER_MENU)
        parameter = input(InputPrompts.ENTER)
        match parameter:
            case '1': destination_menu(customer_id)
            case '2': BookPackage.cancel_booking(customer_id)
            case '3': BookPackage.show_booking_package(customer_id)
            case '4': break
            case _: print(PrintPrompts.INVALID_PROMPT)