'''Controller for adding package'''

import logging
from handlers.package_handler import PackageHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from config.prompt import PrintPrompts
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class CreatePackageController:
    '''Class for Creating new package'''
    def __init__(self) -> None:
        self.pack_handler = PackageHandler()

    @handle_custom_errors
    def create_package(self, package_data):
        '''Method for creating new package'''
        logger.info(f'{get_request_id()} - Creating new package')
        package_id = self.pack_handler.add_package(package_data)
        return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.PACKAGE_ADDED, package_id).jsonify_data, 201

    