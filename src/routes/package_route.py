'''Routes for package related operations'''

import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.package_schema import PackageSchema, PackageUpdateSchema
from controllers.package_controller.create_package_controller import CreatePackageController
from controllers.package_controller.get_package_controller import GetPackageController
from controllers.package_controller.update_package_controller import UpdatePackageController
from utils.role_based_access import role_based_access
from utils.logging_request_id import get_request_id
from utils.role_mapping import Role

logger = logging.getLogger(__name__)

blp_package = Blueprint("Package", __name__, description = "Admin methods on package")

@blp_package.route("/v1/packages")
class Packages(MethodView):
    '''
    Route for:-
    - Getting all packages
    - Posting a new package
    '''

    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.response(200, PackageSchema(many=True))
    def get(self):
        '''Getting all packages'''
        logger.info(f"{get_request_id()} -  route for getting packages")
        value = GetPackageController().get_package_details()
        return value

    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.arguments(PackageSchema)
    def post(self, package_data): 
        '''Creating new package'''
        print("hyhy")
        logger.info(f"{get_request_id()} -  route for posting packages") 
        return CreatePackageController().create_package(package_data)

@blp_package.route("/v1/packages/<string:package_id>")
class Package(MethodView):
    '''
    Route for:-
    - Updating a package
    '''    
    @blp_package.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_package.arguments(PackageUpdateSchema)
    def put(self, package_data, package_id):
        '''Updating package with given package id'''
        logger.info(f"{get_request_id()} -  route for login")
        return UpdatePackageController().update_package(package_data, package_id)
