
from flask_smorest import abort
from handlers.auth_handler.registration_handler import RegistrationHandler
from utils.exception import UserAlreadyExists

class RegistrationController:
    def __init__(self) -> None:
        self.reg_handler = RegistrationHandler()

    def register(self, user_data):
        try:
            self.reg_handler.save_customer(user_data["username"], user_data["password"], user_data["name"], user_data["mobile_number"], user_data["gender"], user_data["age"], user_data["email"])
       
            return {
                "name": user_data["name"],
                "message": "registered"
            }
        except UserAlreadyExists:
            abort(409, message="User already exists")
        