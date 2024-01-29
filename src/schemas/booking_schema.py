from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class GetBookingSchema(Schema):
    booking_id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    mobile_number = fields.Str(dump_only=True)
    start_date = fields.Str(dump_only=True)
    end_date = fields.Str(dump_only=True)
    number_of_people = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    booking_date = fields.Str(dump_only=True)
    trip_status = fields.Str(dump_only=True)

class CreateBookingSchema(Schema):
    package_id = fields.Str(required = True, validate=validate.Regexp(RegularExp.UUID))
    days_night = fields.Str(required=True, validate=validate.Regexp(RegularExp.DURATION))
    price = fields.Int(required=True)
    name = fields.Str(required=True, validate=validate.Regexp(RegularExp.NAME))
    mobile_number = fields.Str(required=True, validate=validate.Regexp(RegularExp.MOBILE_NUMBER))
    start_date = fields.Str(required=True)
    number_of_people = fields.Int(required=True)
    email = fields.Str(required=True, validate=validate.Regexp(RegularExp.EMAIL))