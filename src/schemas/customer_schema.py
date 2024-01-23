from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class ProfileSchema(Schema):
    name = fields.Str(dump_only=True)
    mobile_number = fields.Str(dump_only=True)
    gender = fields.Str(dump_only=True)
    age = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)