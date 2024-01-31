
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_parameter_validation import ValidateParameters, Json
from schemas.itinerary_schema import ItinerarySchema, ItineraryUpdateSchema
from controllers.itinerary_controller.create_itinerary_controller import CreateItineraryController
from controllers.itinerary_controller.get_itinerary_controller import GetItineraryController
from controllers.itinerary_controller.update_itinerary_controller import UpdateItineraryController
from utils.role_based_access import role_based_access
from utils.role_mapping import Role

blp_itinerary = Blueprint("Itinerary", __name__, description = "Admin methods on itinerary")

@blp_itinerary.route("/itineraries")
class Itineraries(MethodView):
    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access([Role.ADMIN, Role.CUSTOMER])
    # @blp_itinerary.response(200, ItinerarySchema(many=True))
    def get(self):
        
        return GetItineraryController().get_itinerary_details()
    
    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.arguments(ItinerarySchema)
    def post(self, user_data):
        return CreateItineraryController().create_new_itinerary(user_data)

@blp_itinerary.route("/itineraries/<string:itinerary_id>")
class Itinerary(MethodView):
    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.arguments(ItineraryUpdateSchema)
    def put(self, itinerary_data, itinerary_id):
        return UpdateItineraryController().change_itinerary(itinerary_data, itinerary_id)
    