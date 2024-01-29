from handlers.review_handler import ReviewHandler
from utils.exception import DBException
from utils.custom_response import CustomSuccessResponse
from config.status_code import StatusCodes
from config.prompt import PrintPrompts

class CreateReviewController:

    def add_review(self, review_data, package_id): 
        ReviewHandler().add_review( review_data["name"], review_data["comment"], review_data["booking_id"], package_id)
        return CustomSuccessResponse(StatusCodes.CREATED, PrintPrompts.ADDED).jsonify_data
