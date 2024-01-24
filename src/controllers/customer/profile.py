from handlers.customer_handler.customer_info import ProfileHandler

class CustomerController:

    def __init__(self, customer_id):
        self.profile_handler = ProfileHandler(customer_id)

    def get_details(self):
        details = self.profile_handler.display_details()
        return details
        
    def update_details(self):
        pass