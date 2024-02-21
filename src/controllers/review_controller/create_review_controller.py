'''Controller for adding review'''

import logging
from handlers.review_handler import ReviewHandler
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.error_handler import handle_custom_errors

logger = logging.getLogger(__name__)

class CreateReviewController:
    '''Class for adding new review'''
    def __init__(self) -> None:
        self.review_handler = ReviewHandler()

    @handle_custom_errors
    def add_review(self, review_data, package_id):
        '''Method for adding new review'''
        logger.info(f'{get_request_id()} - Adding new review') 
        self.review_handler.add_review( review_data, package_id)
        return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.ADDED).jsonify_data, 201
