
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.admin_schema import ItinerarySchema, ItineraryUpdateSchema
from controllers.admin.itinerary import ItineraryController
from utils.role_based_access import role_based_access
from utils.role_mapping import Role

blp_itinerary = Blueprint("Itinerary", __name__, description = "Admin methods on itinerary")

@blp_itinerary.route("/itinerary")
class Itinerary(MethodView):
    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.response(200, ItinerarySchema(many=True))
    def get(self):
        itinerary_obj = ItineraryController()
        value = itinerary_obj.get_itinerary()
        return value
    
    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.arguments(ItinerarySchema)
    def post(self, user_data):
        itinerary_obj = ItineraryController()
        value = itinerary_obj.create_itinerary(user_data)
        return value

@blp_itinerary.route("/itinerary/<string:itinerary_id>")
class UpdateItineraryDetail(MethodView):

    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.arguments(ItineraryUpdateSchema)
    def put(self, itinerary_data, itinerary_id):
        itinerary_obj = ItineraryController()
        value = itinerary_obj.update_itinerary(itinerary_data, itinerary_id)
        return value
    