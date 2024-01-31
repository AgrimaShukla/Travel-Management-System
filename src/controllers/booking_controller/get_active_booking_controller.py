from flask_jwt_extended import get_jwt
from handlers.booking_handler import BookingHandler
from config.prompt import PrintPrompts
from datetime import datetime, timedelta
from utils.exception import DBException
from utils.custom_response import CustomError

class GetActiveBookingController:
    
    def get_active_booking(self):
        try:
            jwt = get_jwt()
            user_id = jwt.get('sub')
            booking_details = BookingHandler().get_active_booking((user_id, PrintPrompts.ACTIVE, datetime.now().date() + timedelta(days = 7)))
            
            return booking_details
        except DBException as err:
            print(err)
            CustomError(err[0], err[1])
