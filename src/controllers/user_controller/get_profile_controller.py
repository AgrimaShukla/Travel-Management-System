'''Controller for fetching user profile'''

import logging
from flask_jwt_extended import get_jwt_identity
from handlers.profile_handler import ProfileHandler
from utils.error_handler import handle_custom_errors
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class GetProfileController:
    '''Class for fetching user profile'''
    def __init__(self):
        self.profile_handler = ProfileHandler()

    @handle_custom_errors
    def get_profile_details(self):
        '''Getting user profile details'''
        logger.info(f'{get_request_id()} - Get user profile')
        user_id = get_jwt_identity()
        details = self.profile_handler.get_user_details((user_id, ))
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.SUCCESS, details).jsonify_data
        
