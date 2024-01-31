from marshmallow import Schema, fields, validate, validates
from config.regex_value import RegularExp
from utils.custom_response import CustomError
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

class DateSchema(Schema):
    ...
    start_date = fields.Str(required=True)

    @staticmethod
    @validates('start_date')
    def validate_date(start_date) -> None:
    
        while True:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                if start_date > datetime.now().date():
                    return start_date
                elif start_date <= datetime.now().date():
                    CustomError(StatusCodes.UNPROCESSABLE_CONTENT, PrintPrompts.INVALID_DATE)
                else: 
                    CustomError(StatusCodes.UNPROCESSABLE_CONTENT, PrintPrompts.INVALID_DATE_FORMAT)
            except ValueError:
                CustomError(StatusCodes.UNPROCESSABLE_CONTENT, PrintPrompts.INVALID_DATE)

class CreateBookingSchema(Schema):
    package_id = fields.Str(required = True, validate=validate.Regexp(RegularExp.UUID))
    days_night = fields.Str(required=True, validate=validate.Regexp(RegularExp.DURATION))
    price = fields.Int(required=True)
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
    