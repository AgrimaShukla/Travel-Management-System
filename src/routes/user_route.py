
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.profile_schema import GetProfileSchema, UpdateProfileSchema
from controllers.profile_controller.get_profile_controller import GetProfileController
from controllers.profile_controller.update_profile_controller import UpdateProfileController
from controllers.profile_controller.delete_profile_controller import DeleteProfileController
from utils.role_based_access import role_based_access
from utils.role_mapping import Role


blp_profile = Blueprint("Profile", __name__, description="View profile for Customer")

@blp_profile.route("/profile")
class Profile(MethodView):

    @blp_profile.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_profile.response(200, GetProfileSchema)
    def get(self):
        return GetProfileController().get_profile_details()


@blp_profile.route("/user/<string:user_id>")
class ChangeUser(MethodView):

    @blp_profile.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_profile.arguments(UpdateProfileSchema)
    def put(self, user_data, user_id):
        return UpdateProfileController().update_profile_details(user_data)
    
    @blp_profile.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    def delete(self, user_id):
        return DeleteProfileController().delete_user()
    