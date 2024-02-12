import logging
from flask_jwt_extended import get_jwt_identity
from handlers.profile_handler import ProfileHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from config.status_code import StatusCodes
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class UpdateProfileController:
    '''Class for updating user details'''
    def __init__(self):
        self.profile_handler = ProfileHandler()

    @handle_custom_errors
    def update_profile_details(self, user_data):
        '''Method for upadting user profile'''
        logger.info(f'{get_request_id()} - Updating user profile')
        user_id = get_jwt_identity()
        user_tuple = (user_data["name"], user_data["mobile_number"], user_data["gender"], user_data["age"], user_data["email"], user_id)
        self.profile_handler.update_details(user_tuple)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data
        