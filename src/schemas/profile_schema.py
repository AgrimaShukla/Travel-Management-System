from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class GetProfileSchema(Schema):
    name = fields.Str(dump_only=True)
    mobile_number = fields.Str(dump_only=True)
    gender = fields.Str(dump_only=True)
    age = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)

class UpdateProfileSchema(Schema):
    name = fields.Str(required=True, validate=validate.Regexp(RegularExp.NAME))
    mobile_number = fields.Str(required=True, validate=validate.Regexp(RegularExp.MOBILE_NUMBER))
    gender = fields.Str(required=True, validate=validate.Regexp(RegularExp.GENDER))
    age = fields.Str(required=True, validate=validate.Regexp(RegularExp.AGE))
    email = fields.Str(required=True, validate=validate.Regexp(RegularExp.EMAIL))