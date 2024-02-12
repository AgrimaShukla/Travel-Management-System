'''Routes for review related operations'''

import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.review_schema import GetReviewSchema, PostReviewSchema
from utils.role_based_access import role_based_access
from utils.role_mapping import Role
from controllers.review_controller.get_review_controller import GetReviewController
from controllers.review_controller.create_review_controller import CreateReviewController
from utils.logging_request_id import get_request_id

logger = logging.getLogger(__name__)

blp_review = Blueprint("Review", __name__, description = "Customer Review")

@blp_review.route("/package/<string:package_id>/reviews")
class Review(MethodView):
    '''
    Route for:-
    - Fetching all reviews for a package
    - Posting new review for a package
    '''
    @blp_review.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_review.response(200, GetReviewSchema(many=True))
    def get(self, package_id):
        '''Getting all reviews for a package'''
        logger.info(f"{get_request_id()} -  route for getting reviews for a particular package")
        return GetReviewController().get_review(package_id)
    
    @blp_review.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_review.arguments(PostReviewSchema)
    def post(self, review_data, package_id):
        '''Creating a new review for a package'''
        logger.info(f"{get_request_id()} -  route for posting new review for a package")
        return CreateReviewController().add_review(review_data, package_id)
