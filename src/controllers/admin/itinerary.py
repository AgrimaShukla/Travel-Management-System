from flask_smorest import abort
from handlers.admin_handler.itinerary import ItineraryHandler
from utils.exception import DataNotFound, PackageDoesNotExist

class ItineraryController:
    def __init__(self) -> None:
        self.iti_handler = ItineraryHandler()

    def get_itinerary(self):
        try:
            result = self.iti_handler.fetch_itinerary()
            return result
        except DataNotFound:
            abort(404, message = "No itinerary found")

    def create_itinerary(self, itinerary_data):
        try:
            self.iti_handler.add_itinerary(itinerary_data["package_id"], itinerary_data["day"], itinerary_data["city"], itinerary_data["description"])
            return {"message": "Itinerary created"}, 201
        except PackageDoesNotExist:
            abort(404, message = "No package found with given id")
    
    def update_itinerary(self, itinerary_data, itinerary_id):
        try:
            itinerary_tuple = (itinerary_data['day'], itinerary_data['city'], itinerary_data['description'], itinerary_id)
            self.iti_handler.update_in_itinerary(itinerary_tuple)
            return {"message": "Itinerary updated"}, 200
        except DataNotFound:
            abort(404, message='No Itinerary found')