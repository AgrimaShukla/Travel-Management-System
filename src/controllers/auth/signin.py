from flask_smorest import abort
from handlers.auth_handler.login_handler import LoginHandler
from utils.exception import DBException

from utils.custom_response import CustomError
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class LoginController:

    def __init__(self) -> None:
        self.auth_handler = LoginHandler()

    def login(self, user_data):
        try:
            access_token, refresh_token = self.auth_handler.user_authentication(user_data)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "message": "You are logged in"
            }
        except DBException as err:
            return CustomError(StatusCodes.UNAUTHORIZED, err).jsonify_data



