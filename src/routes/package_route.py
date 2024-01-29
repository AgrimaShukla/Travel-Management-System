
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.package_schema import PackageSchema, PackageUpdateSchema
from controllers.package_controller.create_package_controller import CreatePackageController
from controllers.package_controller.get_package_controller import GetPackageController
from controllers.package_controller.update_package_controller import UpdatePackageController

from utils.role_based_access import role_based_access
from utils.role_mapping import Role
blp_package = Blueprint("Package", __name__, description = "Admin methods on package")

@blp_package.route("/packages")
class Packages(MethodView):
    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.response(200, PackageSchema(many=True))
    def get(self):
        return GetPackageController().get_package_details()

    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.arguments(PackageSchema)
    def post(self, package_data):  
        return CreatePackageController().create_package(package_data)

@blp_package.route("/packages/<string:package_id>")
class Package(MethodView):    
    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.arguments(PackageUpdateSchema)
    def put(self, package_data, package_id):
        return UpdatePackageController().update_package(package_data, package_id)
