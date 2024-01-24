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

    def create_package(self, package_data):
        self.pack_handler.add_package(package_data["package_name"], package_data["duration"], package_data["category"], package_data["price"], package_data["status"])
        return {"message": "Package created"}, 201
    
    def update_package(self, package_data, package_id):
        try:
            package_tuple = (package_data['package_name'], package_data['duration'], package_data['category'], package_data['price'], package_data['status'], package_id)
            self.pack_handler.update_in_package(package_tuple)
            return {"message": "Package updated"}, 200
        except DataNotFound:
            abort(404, message='No package found')
