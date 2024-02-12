'''Routes for User related operations'''

import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.profile_schema import GetProfileSchema, UpdateProfileSchema
from controllers.user_controller.get_profile_controller import GetProfileController
from controllers.user_controller.update_profile_controller import UpdateProfileController
from controllers.user_controller.delete_user_controller import DeleteUserController
from utils.role_based_access import role_based_access
from utils.role_mapping import Role
from utils.logging_request_id import get_request_id

logger = logging.getLogger(__name__)

blp_profile = Blueprint("Profile", __name__, description="View profile for Customer")

@blp_profile.route("/profile")
class Profile(MethodView):
    '''
    Route for:- 
    - Getting user information
    '''

    @blp_profile.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_profile.response(200, GetProfileSchema)
    def get(self):
        '''Fetch user details'''
        logger.info(f"{get_request_id()} -  route for getting user profile")
        return GetProfileController().get_profile_details()


@blp_profile.route("/user/<string:user_id>")
class ChangeUser(MethodView):
    '''
    Route for:-
    - Updating user information
    - Deleting user profile
    '''

    @blp_profile.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_profile.arguments(UpdateProfileSchema)
    def put(self, user_data, user_id):
        '''Updating user detail'''
        logger.info(f"{get_request_id()} -  route for updating user profile")
        return UpdateProfileController().update_profile_details(user_data)
    
    @blp_profile.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    def delete(self, user_id):
        '''Deleting a user account'''
        logger.info(f"{get_request_id()} -  route for deleting account")
        return DeleteUserController().delete_user(user_id)
    