from handlers.review_handler import ReviewHandler
from utils.exception import DBException
from utils.custom_response import CustomError
from config.status_code import StatusCodes

class GetReviewController:
    
    def get_review(self, package_id):
        try:
            reviews = ReviewHandler().get_reviews(package_id)
            return reviews
        except DBException as err:
             return CustomError(StatusCodes.NOT_FOUND, err).jsonify_data
