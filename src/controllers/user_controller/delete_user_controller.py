'''Controller for deleting user'''

import logging
from flask_jwt_extended import get_jwt_identity
from handlers.profile_handler import ProfileHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from config.prompt import PrintPrompts
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class DeleteUserController:
    '''Class for deleting user'''
    def __init__(self):
        self.profile_handler = ProfileHandler()

    @handle_custom_errors
    def delete_user(self, user_id):
        '''Deleting a particular user'''
        
        logger.info(f'{get_request_id()} - Deleting user')
        user_id = get_jwt_identity()
        self.profile_handler.delete_user((user_id, ))
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.ACCOUNT_DELETED).jsonify_data
        