'''Routes for login, registering and logout'''
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.auth_schema import LoginSchema, LoginSuccessSchema, RegisterSchema
from controllers.auth.signin_controller import LoginController
from controllers.auth.signup_controller import RegistrationController
from controllers.auth.logout_controller import LogoutController
from controllers.auth.refresh_controller import RefreshController
from utils.logging_request_id import get_request_id
from flask_jwt_extended import jwt_required

logger = logging.getLogger(__name__)

blp_auth = Blueprint("Authentication", "authentication", description = "Authentication of users")

@blp_auth.route("/v1/signin")
class Login(MethodView):
    '''
    Route for:- 
    - Login for user
    '''

    @blp_auth.arguments(LoginSchema)
    @blp_auth.response(200, LoginSuccessSchema)
    def post(self, user_data):
        '''User Login'''
        logger.info(f"{get_request_id()} -  route for login")
        return LoginController().login(user_data)


@blp_auth.route("/v1/signup")
class registration(MethodView):
    '''
    Route for:-
    - Registering user
    '''

    @blp_auth.arguments(RegisterSchema)
    def post(self, user_data):
        '''Signup for user'''
        logger.info(f"{get_request_id()} -  route for signup")
        return RegistrationController.register(user_data)
        

@blp_auth.route("/v1/logout")
class UserLogout(MethodView):
   '''
   Route for:-
   - Logout for user
   '''
   
#    @jwt_required()
   @blp_auth.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
   @jwt_required()
   def post(self):
       '''Logout user'''
       logger.info(f"{get_request_id()} -  route for logout")
       print("heyyy")
       return LogoutController().logout()
   
@blp_auth.route("/v1/refresh")
class Refresh(MethodView):
    '''
    Route for:-
    - Refresh token
    '''
    @jwt_required(refresh=True)
    @blp_auth.response(200, LoginSuccessSchema)
    @blp_auth.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self):  
        '''Refresh token'''
        return RefreshController().refresh()