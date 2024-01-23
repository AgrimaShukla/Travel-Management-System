'''This module handles user preference for the packages'''

from config.prompt import PrintPrompts, InputPrompts
from view.customer_view.booking_view.booking_module_view import BookingPackageView
from view.customer_view.customer_info import CustomerDetails
from view.customer_view.review_module import ReviewViews
from view.customer_view.booking_view.view_package import view_package
from controller.customer_controller.menu_controller import MenuController
class UserMenu:
    '''Displaying user menu'''

    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        self.obj_booking = BookingPackageView()
        self.obj_customer = CustomerDetails(self.customer_id)
        self.obj_review = ReviewViews()
        self.menu_cont = MenuController()

    def category_menu(self, destination: str) -> None:
        '''User can choose category'''
        while True:
            value = self.menu_cont.get_category()
            my_dict = {i + 1: value for i, value in enumerate(value)}
            tuple_of_values = tuple(value[0] for value in my_dict.values())
            print(PrintPrompts.CATEGORY_PROMPT.format(*tuple_of_values))
            option = int(input(InputPrompts.ENTER))
            
            if option in tuple(my_dict.keys()):
                self.day_menu(destination, my_dict[option], self.customer_id)
            elif option == 4:
                break
            else:
                print(PrintPrompts.INVALID_PROMPT)

    def destination_menu(self) -> None:
        '''User can choose destination'''
        while True:
            

            value = self.menu_cont.get_package_name()
            my_dict = {i + 1: value for i, value in enumerate(value)}
            tuple_of_values = tuple(value[0] for value in my_dict.values())
            print(PrintPrompts.DESTINATION_PROMPT.format(*tuple_of_values))
            option = int(input(InputPrompts.ENTER))
            if option in tuple(my_dict.keys()):
                self.category_menu(my_dict[option])
            elif option == 6:
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
                case '5': self.obj_customer.enter_details()
                case '6': self.obj_review.show_data(self.customer_id)
                case '7': break
                case _: print(PrintPrompts.INVALID_PROMPT)
                
    def day_menu(self, dest_option: str, category_option: str, customer_id: str) -> None:
        '''User can choose days'''
        while True:
            value = self.menu_cont.get_duration()
            my_dict = {i + 1: value for i, value in enumerate(value)}
            tuple_of_values = tuple(value[0] for value in my_dict.values())
            print(PrintPrompts.DAY_PROMPT.format(*tuple_of_values))
            option = int(input(InputPrompts.ENTER))
            if option in tuple(my_dict.keys()):
                view_package(dest_option, category_option, my_dict[option], customer_id)
            elif option == 4:
                break
            else:
                print(PrintPrompts.INVALID_PROMPT)
