from flask import jsonify
from dataclasses import dataclass, field
from typing import NamedTuple

@dataclass
class CustomError(Exception):
    status: NamedTuple
    description: str
    code: int = field(init=False)

    def __post_init__(self) -> None:
        self.code = self.status.code

    @property
    def jsonify_data(self):
        return jsonify(
            {
            "status_code": self.status.code,
            "status": self.status.status,
            "description": self.description
            }
        )


class ApplicationException(CustomError):
    pass

class DBException(CustomError):
    pass