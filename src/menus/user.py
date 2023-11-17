'''This module handles user preference for the packages'''

from src.config.prompt import PrintPrompts, InputPrompts
from src.controllers.customer_controller.booking_module import view_package, show_itinerary_package, cancel_booking
from src.controllers.customer_controller.customer_info import show_details, update_details
from src.controllers.customer_controller.review_module import show_data

def day_menu(dest_option: str, category_option: str, customer_id: str) -> None:
    '''User can choose days'''
    while True:
        print(PrintPrompts.DAY_PROMPT)
        option = input(InputPrompts.ENTER)
        if option in ('1', '2', '3'):
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
        if option in ('1', '2', '3'):
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
        if option in ('1', '2', '3', '4', '5'):
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
            case '2': cancel_booking(customer_id)
            case '3': show_itinerary_package(customer_id)
            case '4': show_details(customer_id)
            case '5': update_details(customer_id)
            case '6': show_data(customer_id)
            case '7': break
            case _: print(PrintPrompts.INVALID_PROMPT)
            