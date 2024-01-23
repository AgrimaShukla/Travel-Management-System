
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.admin_schema import ItinerarySchema
# from controller.admin_controller.itinerary import ItineraryController
from utils.role_based_access import role_based_access
from utils.role_mapping import Role

blp_itinerary = Blueprint("Itinerary", __name__, description = "Admin methods on itinerary")

@blp_itinerary.route("/itinerary")
class Itinerary(MethodView):
    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.response(200, ItinerarySchema(many=True))
    def get(self):
        package_obj = ItineraryController()
        value = package_obj.fetch_itinerary()
        if value:
            return value
        else:
            abort(500, message = "Internal server error") 

    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.arguments(ItinerarySchema)
    def post(self, user_data):
        package_obj = ItineraryController()
        value = package_obj.add_itinerary(user_data["day"], user_data["city"], user_data["description"], user_data["package_id"])
        
        if value:
            return {
                "message": "Inserted"
            }
        else:
            abort(500, message = "Internal server error")