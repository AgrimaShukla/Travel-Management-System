
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.admin_schema import PackageSchema, PackageUpdateSchema
from controllers.admin.package import PackageController
# from controller.registration_controller import Registration
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
        value = package_obj.get_package()
        return value

    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.arguments(PackageSchema)
    def post(self, package_data):
        package_obj = PackageController()
        value = package_obj.create_package(package_data)   
        return value

@blp_package.route("/package/<string:package_id>")
class UpdatePackageDetails(MethodView):    
    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.arguments(PackageUpdateSchema)
    def put(self, package_data, package_id):
        package_obj = PackageController()
        value = package_obj.update_package(package_data, package_id)
        return value
