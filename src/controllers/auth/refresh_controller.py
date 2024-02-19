'''Controller for refresh token'''

import logging
from utils.token import Token
from flask_jwt_extended import get_jwt
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.error_handler import handle_custom_errors
from config.prompt import PrintPrompts

logger = logging.getLogger(__name__)

class RefreshController:
    '''Class for refresh token'''

    def __init__(self) -> None:
        self.token_obj = Token()

    @handle_custom_errors
    def refresh(self):
        '''Method to revoke token and refresh token'''

        logging.info(f"{get_request_id()} - User logging out")
        claims = get_jwt()
        user_id = claims.get('sub')
        mapped_role = claims.get('game')
        self.token_obj.revoke_token(get_jwt())
        access_token, refresh_token = self.token_obj.generate_token(mapped_role, user_id, False)
        token = [{
            "access_token": access_token,
            "refresh_token": refresh_token
        }]
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.REFRESH_TOKEN, token).jsonify_data