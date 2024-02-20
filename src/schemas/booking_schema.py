from marshmallow import Schema, fields, validate, validates_schema
from config.regex_value import RegularExp
from utils.custom_error_response import ApplicationException
from utils.custom_error_response import CustomError
from config.status_code import StatusCodes
from datetime import datetime
from config.prompt import PrintPrompts

class GetBookingSchema(Schema):
    booking_id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    mobile_number = fields.Str(dump_only=True)
    start_date = fields.Str(dump_only=True)
    end_date = fields.Str(dump_only=True)
    no_of_people = fields.Int(dump_only=True)
    email = fields.Str(dump_only=True)
    booking_date = fields.Str(dump_only=True)
    trip_status = fields.Str(dump_only=True)


class CreateBookingSchema(Schema):
    package_id = fields.Str(required = True, validate=validate.Regexp(RegularExp.UUID))
    days_night = fields.Str(required=True, validate=validate.Regexp(RegularExp.DURATION))
    name = fields.String(required=True, validate=validate.Regexp(RegularExp.NAME))
    mobile_number = fields.Str(required=True, validate=validate.Regexp(RegularExp.MOBILE_NUMBER))
    start_date = fields.Str(required=True)
    end_date = fields.Str(required=True)
    number_of_people = fields.Int(required=True)
    email = fields.Str(required=True, validate=validate.Regexp(RegularExp.EMAIL))


class UpdateBookingSchema(Schema):
    name = fields.String(required=True, validate=validate.Regexp(RegularExp.NAME))
    mobile_number = fields.Str(required=True, validate=validate.Regexp(RegularExp.MOBILE_NUMBER))
    start_date = fields.Str(required=True)
    end_date = fields.Str(required=True)
    number_of_people = fields.Int(required=True)
    email = fields.Str(required=True, validate=validate.Regexp(RegularExp.EMAIL))
