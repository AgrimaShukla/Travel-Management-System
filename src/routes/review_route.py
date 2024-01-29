from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.review_schema import GetReviewSchema, PostReviewSchema
from utils.role_based_access import role_based_access
from utils.role_mapping import Role
from controllers.review_controller.get_review_controller import GetReviewController
from controllers.review_controller.create_review_controller import CreateReviewController

blp_review = Blueprint("Review", __name__, description = "Customer Review")

@blp_review.route("/package/<string:package_id>/reviews")
class Review(MethodView):
    
    @blp_review.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_review.response(200, GetReviewSchema(many=True))
    def get(self, package_id):
        return GetReviewController().get_review(package_id)
    
    @blp_review.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_review.arguments(PostReviewSchema)
    def post(self, review_data, package_id):
        return CreateReviewController().add_review(review_data, package_id)
