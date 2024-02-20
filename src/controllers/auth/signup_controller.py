'''Controller for registering user'''

import logging
from handlers.auth_handler.registration_handler import RegistrationHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from config.prompt import PrintPrompts
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class RegistrationController:
    '''Class for user registration'''

    def __init__(self) -> None:
        self.reg_handler = RegistrationHandler()

    @handle_custom_errors
    def register(self, user_data): 
        '''Registering new user'''
        
        logger.info(f'{get_request_id()} - New user registering') 
        user_id = self.reg_handler.save_customer(user_data["username"], user_data["password"], user_data["name"], user_data["mobile_number"], user_data["gender"], user_data["age"], user_data["email"])
        user_data = [{
            "user_id": user_id
        }]
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.REGISTERED, user_data).jsonify_data
       