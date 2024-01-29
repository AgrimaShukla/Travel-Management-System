from flask_smorest import abort
from handlers.package_handler import PackageHandler
from utils.custom_response import CustomSuccessResponse, CustomError
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class CreatePackageController:

    def __init__(self) -> None:
        self.pack_handler = PackageHandler()

    def create_package(self, package_data):
        self.pack_handler.add_package(package_data["package_name"], package_data["duration"], package_data["category"], package_data["price"], package_data["status"])
        return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.PACKAGE_ADDED).jsonify_data

    