from flask_smorest import abort
from handlers.admin_handler.package import PackageHandler
from utils.exception import DataNotFound

class PackageController:
    def __init__(self) -> None:
        self.pack_handler = PackageHandler()

    def get_package(self):
        try:
            result = self.pack_handler.fetch_package()
            return result
        except DataNotFound:
            abort(404, message = "No package found")

    def create_package(self, user_data):
        self.pack_handler.add_package(user_data["package_name"], user_data["duration"], user_data["category"], user_data["price"], user_data["status"])
        return {"message": "Package created"}, 201
    