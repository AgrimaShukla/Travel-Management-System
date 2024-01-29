from flask_smorest import abort
from handlers.package_handler import PackageHandler
from utils.exception import DBException
from config.prompt import PrintPrompts
from utils.custom_response import CustomError
from config.status_code import StatusCodes

class GetPackageController:
    def __init__(self) -> None:
        self.pack_handler = PackageHandler()

    def get_package_details(self):
        try:
            result = self.pack_handler.fetch_package()
            return result
        except DBException as err:
            return CustomError(StatusCodes.NOT_FOUND, err).jsonify_data
        