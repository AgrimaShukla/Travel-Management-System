'''This module handles user preference for the packages'''

from config.prompt import PrintPrompts, InputPrompts
from controllers.customer_controller.booking.booking_module import BookPackage
from controllers.customer_controller.booking.booking_package import view_package
from controllers.customer_controller.customer_info import CustomerDetails
from controllers.customer_controller.review_module import Review

class UserMenu:
    '''Displaying user menu'''

    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        self.obj_booking = BookPackage()
        self.obj_customer = CustomerDetails(self.customer_id)
        self.obj_review = Review()

    def category_menu(self, dest_option: str) -> None:
        '''User can choose category'''
        while True:
            print(PrintPrompts.CATEGORY_PROMPT)
            option = input(InputPrompts.ENTER)
            if option in ('1', '2', '3'):
                self.day_menu(dest_option, option, self.customer_id)
            elif option == '4':
                break
            else:
                print(PrintPrompts.INVALID_PROMPT)

    def destination_menu(self) -> None:
        '''User can choose destination'''
        while True:
            print(PrintPrompts.DESTINATION_PROMPT)
            option = input(InputPrompts.ENTER)
            if option in ('1', '2', '3', '4', '5'):
                self.category_menu(option)
            elif option == '6':
                break
            else:
                print(PrintPrompts.INVALID_PROMPT)

    def user_menu(self) -> None:
        '''To show the user menu'''
        while True:
            print(PrintPrompts.USER_MENU)
            parameter = input(InputPrompts.ENTER)
            match parameter:
                case '1': self.destination_menu()
                case '2': self.obj_booking.cancel_booking(self.customer_id)
                case '3': self.obj_booking.show_itinerary_package(self.customer_id)
                case '4': self.obj_customer.show_details()
                case '5': self.obj_customer.update_details()
                case '6': self.obj_review.show_data(self.customer_id)
                case '7': break
                case _: print(PrintPrompts.INVALID_PROMPT)
                
    @staticmethod
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
