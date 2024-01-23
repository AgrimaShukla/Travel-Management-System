from flask_smorest import abort
from handlers.auth_handler.login_handler import LoginHandler
from utils.exception import InvalidUsernameorPassword

class LoginController:

    def __init__(self) -> None:
        self.auth_handler = LoginHandler()

    def login(self, user_data):
        try:
            token = self.auth_handler.user_authentication(user_data)
            return token
        except InvalidUsernameorPassword:
            abort(401, message="Invalid username or password")


