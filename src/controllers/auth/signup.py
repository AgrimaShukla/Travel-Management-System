
from flask_smorest import abort
from handlers.auth_handler.registration_handler import RegistrationHandler
from utils.exception import DBException
from utils.custom_response import CustomError, CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class RegistrationController:
    def __init__(self) -> None:
        self.reg_handler = RegistrationHandler()

    def register(self, user_data):
        try:
            self.reg_handler.save_customer(user_data["username"], user_data["password"], user_data["name"], user_data["mobile_number"], user_data["gender"], user_data["age"], user_data["email"])
            return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.REGISTERED).jsonify_data
        except DBException as err:
            return CustomError(StatusCodes.CONFLICT, str(err)).jsonify_data

        