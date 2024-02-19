'''Controller for user logout'''

import logging
from utils.token import Token
from flask_jwt_extended import get_jwt
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.error_handler import handle_custom_errors
from config.prompt import PrintPrompts

logger = logging.getLogger(__name__)

class LogoutController:
    '''Class for user logout'''

    def __init__(self) -> None:
        self.token_obj = Token()

    @handle_custom_errors
    def logout(self):
        '''Method to logout user and revoke token'''

        logging.info(f"{get_request_id()} - User logging out")
        # print(get_jwt())
        self.token_obj.revoke_token(get_jwt())
        print(get_jwt())
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.USER_LOGOUT).jsonify_data