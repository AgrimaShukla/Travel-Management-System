from flask_smorest import abort
from handlers.auth_handler.login_handler import LoginHandler
from utils.exception import InvalidUsernameorPassword
from flask_jwt_extended import create_access_token, create_refresh_token
from utils.role_mapping import Role

class LoginController:

    def __init__(self) -> None:
        self.auth_handler = LoginHandler()

    def login(self, user_data):
        try:
            user_info = self.auth_handler.user_authentication(user_data)
            role = Role.get_role(user_info['role'])
            access_token = create_access_token(identity=user_info['user_id'], fresh=True, additional_claims={"role": role})
            refresh_token = create_refresh_token(identity=user_info['user_id'], additional_claims={"role": role})
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "message": "You are logged in"
            }
        except InvalidUsernameorPassword:
            abort(401, message="Invalid username or password")


