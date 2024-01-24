
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.customer_schema import ProfileSchema
from flask_jwt_extended import get_jwt
from controllers.customer.profile import CustomerController
from utils.role_based_access import role_based_access
from utils.role_mapping import Role


blp_profile = Blueprint("Profile", __name__, description="View profile for Customer")

@blp_profile.route("/profile")
class Profile(MethodView):

    @blp_profile.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.CUSTOMER)
    @blp_profile.response(200, ProfileSchema)
    def get(self):
        jwt = get_jwt()
        customer_id = jwt.get('sub')
        obj_customer = CustomerController(customer_id)
        customer_details = obj_customer.get_details()
        return customer_details

    
