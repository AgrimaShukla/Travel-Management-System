import hashlib
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.auth_schema import LoginSchema, LoginSuccessSchema, RegisterSchema
from flask_jwt_extended import create_access_token, create_refresh_token
from controller.auth_controller import AuthenticationController
from controller.registration_controller import Registration
from flask_jwt_extended import get_jwt, jwt_required
from utils.role_mapping import Role
from blocklist import BLOCKLIST

blp_auth = Blueprint("Authentication", "authentication", description = "Authentication of users")

@blp_auth.route("/signin")
class Login(MethodView):
    @blp_auth.arguments(LoginSchema)
    @blp_auth.response(200, LoginSuccessSchema)
    def post(self, user_data):
        auth_obj = AuthenticationController()
        user_info = auth_obj.user_authentication(user_data["username"])
        pw = hashlib.md5(user_data["password"].encode()).hexdigest()
        role = Role.get_role(user_info['role'])
        if  user_info['password'] == pw:
            access_token = create_access_token(identity=user_info["user_id"], fresh=True, additional_claims={"role": role})
            refresh_token = create_refresh_token(identity=user_info["user_id"], additional_claims={"role": role})
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                # "message": "Successfully logged in"
            }
        else:
            abort(403, message = "User does not exist")

@blp_auth.route("/signup")
class registration(MethodView):
    @blp_auth.arguments(RegisterSchema)
    def post(self, user_data):
        reg_obj = Registration()
        password =  hashlib.md5(user_data["password"].encode()).hexdigest()
        value = reg_obj.save_customer(user_data["username"], password, user_data["name"], user_data["mobile_number"], user_data["gender"], user_data["age"], user_data["email"])
        if value:
            return {
                "name": user_data["name"],
                "message": "registered"
            }
        else:
            abort(500, message = "Interval server Error")

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