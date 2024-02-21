'''Controller for fetching reviews'''

import logging
from handlers.review_handler import ReviewHandler
from utils.error_handler import handle_custom_errors
from config.prompt import PrintPrompts
from utils.logging_request_id import get_request_id
from utils.custom_success_response import CustomSuccessResponse
from config.status_code import StatusCodes

logger = logging.getLogger(__name__)

class GetReviewController:
    '''Class for getting review'''

    def __init__(self) -> None:
        self.review_handler = ReviewHandler()

    @handle_custom_errors
    def get_review(self, package_id):
        '''Method for getting reviews'''
        logger.info(f'{get_request_id} - Fetching reviews') 
        reviews, message = self.review_handler.get_reviews(package_id)
        return CustomSuccessResponse(StatusCodes.OK, message, reviews).jsonify_data
       