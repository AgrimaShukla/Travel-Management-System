from flask_smorest import abort
from handlers.package_handler import PackageHandler
from utils.exception import DBException
from config.prompt import PrintPrompts
from utils.custom_response import CustomSuccessResponse, CustomError
from config.status_code import StatusCodes


class UpdatePackageController:
    def __init__(self) -> None:
        self.pack_handler = PackageHandler()

    def update_package(self, package_data, package_id):
        try:
            package_tuple = (package_data['package_name'], package_data['duration'], package_data['category'], package_data['price'], package_data['status'], package_id)
            self.pack_handler.update_in_package(package_tuple)
            return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data

        except DBException as err:
            return CustomError(StatusCodes.NOT_FOUND, err).jsonify_data

