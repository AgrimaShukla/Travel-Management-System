'''Controller for login user'''

import logging
from handlers.auth_handler.login_handler import LoginHandler
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class LoginController:
    '''Class for user login'''

    def __init__(self) -> None:
        self.auth_handler = LoginHandler()

    def login(self, user_data):
        logging.debug(f'{get_request_id()} - User trying to login')
        access_token, refresh_token = self.auth_handler.user_authentication(user_data)
        token = [{
            PrintPrompts.ACCESS_TOKEN: access_token,
            PrintPrompts.REFRESH_TOKEN: refresh_token
        }]
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.LOGGED_IN, token).jsonify_data
