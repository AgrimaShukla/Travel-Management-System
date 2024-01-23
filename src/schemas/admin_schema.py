from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class PackageSchema(Schema):
    package_id = fields.Str(dump_only=True)
    package_name = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))
    duration = fields.Str(required=True, validate=validate.Regexp(RegularExp.DURATION))
    category = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))
    price = fields.Str(required=True)
    status = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))

class ItinerarySchema(Schema):
    package_id = fields.Str(required=True)
    itineray_id = fields.Str(dump_only=True)
    day = fields.Int(required=True)
    city = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))
    description = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))