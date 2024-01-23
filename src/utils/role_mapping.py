import os
from dotenv import load_dotenv

load_dotenv()

class Role:
    ADMIN = os.getenv('ADMIN')
    CUSTOMER = os.getenv('CUSTOMER')
    
    @classmethod
    def get_role(cls, role):
        if role == "admin":
            return cls.ADMIN
        elif role == "user":
            return cls.CUSTOMER