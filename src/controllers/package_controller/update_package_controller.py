'''Controller for updating package'''

import logging
from handlers.package_handler import PackageHandler
from config.prompt import PrintPrompts
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from utils.logging_request_id import get_request_id
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class UpdatePackageController:
    '''Updating package'''
    def __init__(self) -> None:
        self.pack_handler = PackageHandler()

    @handle_custom_errors
    def update_package(self, package_data, package_id):
        '''Updating a particular package'''
        logger.info(f'{get_request_id()} - Updating a particular package')
        self.pack_handler.update_in_package(package_data, package_id)
        return CustomSuccessResponse(StatusCodes.OK, PrintPrompts.UPDATED).jsonify_data
