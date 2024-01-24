import hashlib
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.auth_schema import LoginSchema, LoginSuccessSchema, RegisterSchema
from flask_jwt_extended import create_access_token, create_refresh_token
from controllers.auth.signin import LoginController
from controllers.auth.signup import RegistrationController
from flask_jwt_extended import get_jwt, jwt_required
from utils.role_mapping import Role
from blocklist import BLOCKLIST

blp_auth = Blueprint("Authentication", "authentication", description = "Authentication of users")

@blp_auth.route("/signin")
class Login(MethodView):
    @blp_auth.arguments(LoginSchema)
    @blp_auth.response(200, LoginSuccessSchema)
    def post(self, user_data):
        login_obj = LoginController()
        token = login_obj.login(user_data)
        return token


@blp_auth.route("/signup")
class registration(MethodView):
    @blp_auth.arguments(RegisterSchema)
    def post(self, user_data):
        reg_obj = RegistrationController()
        result = reg_obj.register(user_data)
        return result
        

@blp_auth.route("/logout")
class UserLogout(MethodView):
   @jwt_required()
   @blp_auth.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
   def post(self):
       jot = get_jwt().get('jti')
       BLOCKLIST.add(jot)
       return {
           "message": "Logged out"
       }       