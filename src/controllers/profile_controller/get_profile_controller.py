from flask_jwt_extended import get_jwt
from handlers.profile_handler import ProfileHandler

class GetProfileController:

    def __init__(self):
        self.profile_handler = ProfileHandler()

    def get_profile_details(self):
        jwt = get_jwt()
        user_id = jwt.get('sub')
        details = self.profile_handler.get_user_details((user_id, ))
        return details
        
