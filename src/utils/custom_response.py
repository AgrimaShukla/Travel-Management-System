from flask import jsonify
from dataclasses import dataclass
from typing import NamedTuple
@dataclass
class CustomError:
    status: NamedTuple
    description: str

    @property
    def jsonify_data(self):
        return jsonify(
            {
            "status_code": self.status.code,
            "status": self.status.status,
            "description": self.description
            }
        )

@dataclass
class CustomSuccessResponse:
    status: NamedTuple = None
    message: str = None

    @property
    def jsonify_data(self):
        return jsonify(
            {
            "status_code": self.status.code,
            "status": self.status.status,
            "message": self.message,
            }
        )