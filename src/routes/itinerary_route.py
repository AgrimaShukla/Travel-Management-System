'''Routes for itinerary related operations'''

import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.itinerary_schema import ItinerarySchema, ItineraryUpdateSchema
from controllers.itinerary_controller.create_itinerary_controller import CreateItineraryController
from controllers.itinerary_controller.get_itinerary_controller import GetItineraryController
from controllers.itinerary_controller.update_itinerary_controller import UpdateItineraryController
from utils.role_based_access import role_based_access
from utils.logging_request_id import get_request_id
from utils.role_mapping import Role

logger = logging.getLogger(__name__)


blp_itinerary = Blueprint("Itinerary2", __name__, description = "Admin methods on itinerary")

@blp_itinerary.route("/v1/itineraries")
class Itineraries(MethodView):
    '''
    Route for:-
    - Getting all Itineraries or filtered itinerary
    - Posting a new itinerary
    '''

    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp_itinerary.response(200, ItinerarySchema(many=True))
    @role_based_access([Role.ADMIN, Role.CUSTOMER])
    def get(self):
        '''Getting all packages'''
        logger.info(f"{get_request_id()} -  route for getting itineraries")
        return GetItineraryController().get_itinerary_details()
    
    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.arguments(ItinerarySchema)
    def post(self, user_data):
        '''Creating new package'''
        logger.info(f"{get_request_id()} -  route for creating itineraries")
        obj = CreateItineraryController()
        response = obj.create_new_itinerary(user_data)
        return response

@blp_itinerary.route("/v1/itineraries/<string:itinerary_id>")
class Itinerary(MethodView):
    '''
    Route for:-
    - Updating itinerary details
    '''

    @blp_itinerary.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @blp_itinerary.arguments(ItineraryUpdateSchema)
    def put(self, itinerary_data, itinerary_id):
        '''Updating itinerary'''
        logger.info(f"{get_request_id()} -  route for updating itinerary")
        return UpdateItineraryController().change_itinerary(itinerary_data, itinerary_id)
    