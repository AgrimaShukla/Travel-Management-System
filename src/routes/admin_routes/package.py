
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.admin_schema import PackageSchema
from flask_jwt_extended import create_access_token, create_refresh_token
from controller.admin_controller.package import PackageController
from controller.registration_controller import Registration
from flask_jwt_extended import get_jwt, jwt_required
from utils.role_based_access import role_based_access
from utils.role_mapping import Role
blp_package = Blueprint("Package", __name__, description = "Admin methods on package")

@blp_package.route("/package")
class Package(MethodView):
    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.response(200, PackageSchema(many=True))
    def get(self):
        package_obj = PackageController()
        value = package_obj.fetch_package()
        if value:
            return value
        else:
            abort(500, message = "Internal server error") 

    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.arguments(PackageSchema)
    def post(self, user_data):
        package_obj = PackageController()
        value = package_obj.add_package(user_data["package_name"], user_data["duration"], user_data["category"], user_data["price"], user_data["status"])
        
        if value:
            return {
                "message": "Inserted"
            }
        else:
            abort(500, message = "Internal server error")
