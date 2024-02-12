'''Controller for fetching package'''

import logging
from flask_smorest import abort
from handlers.package_handler import PackageHandler
from utils.error_handler import handle_custom_errors
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class GetPackageController:
    '''Class getting all packages'''
    def __init__(self) -> None:
        self.pack_handler = PackageHandler()

    @handle_custom_errors
    def get_package_details(self):
        '''Method for getting all packages'''
        logger.info(f'{get_request_id()} - Getting all packages')
        result = self.pack_handler.fetch_package()
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.SUCCESS, result).jsonify_data
