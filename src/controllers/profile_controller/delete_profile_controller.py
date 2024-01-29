from flask_jwt_extended import get_jwt
from handlers.profile_handler import ProfileHandler
from utils.custom_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class DeleteProfileController:

    def __init__(self):
        self.profile_handler = ProfileHandler()

    def delete_user(self):
        jwt = get_jwt()
        user_id = jwt.get('sub')
        self.profile_handler.delete_user((user_id, ))
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.ACCOUNT_DELETED).jsonify_data
        