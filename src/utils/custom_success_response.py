from flask import jsonify
from dataclasses import dataclass, field
from typing import NamedTuple, Optional

@dataclass
class CustomSuccessResponse:
    status: NamedTuple = None
    message: str = None
    data: Optional[list] = None

    @property
    def jsonify_data(self):
        return jsonify(
            {
            "status_code": self.status.code,
            "status": self.status.status,
            "message": self.message,
            "data": self.data
            }
        )
