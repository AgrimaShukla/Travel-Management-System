from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class LoginSchema(Schema):
    username = fields.Str(required=True, validate=validate.Regexp(RegularExp.USERNAME))
    password = fields.Str(load_only=True, validate=validate.Regexp(RegularExp.PASSWORD))

class LoginSuccessSchema(Schema):
    access_token = fields.Str(required=True)
    refresh_token = fields.Str(required=True)
    message = fields.Str(required=True)

class RegisterSchema(LoginSchema):
    user_id = fields.Str(dump_only=True, validate=validate.Regexp(RegularExp.UUID))
    name = fields.String(required=True, validate=validate.Regexp(RegularExp.NAME))
    mobile_number = fields.Str(required=True, validate=validate.Regexp(RegularExp.MOBILE_NUMBER))
    gender = fields.Str(required=True, validate=validate.Regexp(RegularExp.GENDER))
    age = fields.Str(required=True, validate=validate.Regexp(RegularExp.AGE))
    email = fields.Str(required=True, validate=validate.Regexp(RegularExp.EMAIL))

