from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class GetProfileSchema(Schema):
    name = fields.Str(dump_only=True, validate=validate.Regexp(RegularExp.NAME))
    mobile_number = fields.Str(dump_only=True, validate=validate.Regexp(RegularExp.MOBILE_NUMBER))
    gender = fields.Str(dump_only=True, validate=validate.Regexp(RegularExp.GENDER))
    age = fields.Str(dump_only=True, validate=validate.Regexp(RegularExp.AGE))
    email = fields.Str(dump_only=True, validate=validate.Regexp(RegularExp.EMAIL))

class UpdateProfileSchema(Schema):
    name = fields.Str(required=True)
    mobile_number = fields.Str(required=True)
    gender = fields.Str(required=True)
    age = fields.Str(required=True)
    email = fields.Str(required=True)