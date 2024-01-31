from flask_smorest import abort
from handlers.auth_handler.login_handler import LoginHandler
from utils.exception import DBException
from config.prompt import PrintPrompts
from utils.custom_response import CustomError
from config.status_code import StatusCodes


class LoginController:

    def __init__(self) -> None:
        self.auth_handler = LoginHandler()

    def login(self, user_data):
        try:
            access_token, refresh_token = self.auth_handler.user_authentication(user_data)
            return {
                PrintPrompts.ACCESS_TOKEN: access_token,
                PrintPrompts.REFRESH_TOKEN: refresh_token,
                PrintPrompts.MESSAGE: PrintPrompts.LOGGED_IN
            }
        except DBException as err:
            return CustomError(StatusCodes.UNAUTHORIZED, str(err)).jsonify_data



