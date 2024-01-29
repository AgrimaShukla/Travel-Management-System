from flask_jwt_extended import get_jwt
from handlers.profile_handler import ProfileHandler
from utils.custom_response import CustomSuccessResponse, CustomError
from config.status_code import StatusCodes
from config.prompt import PrintPrompts
from utils.exception import DBException
from config.status_code import StatusCodes

class UpdateProfileController:

    def __init__(self):
        self.profile_handler = ProfileHandler()

    def update_profile_details(self, user_data):
        try:
            jwt = get_jwt()
            user_id = jwt.get('sub')
            user_tuple = (user_data["name"], user_data["mobile_number"], user_data["gender"], user_data["age"], user_data["email"], user_id)
            self.profile_handler.update_details(user_tuple)
            return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data
        except DBException as err:
            return CustomError(StatusCodes.CONFLICT, str(err)).jsonify_data