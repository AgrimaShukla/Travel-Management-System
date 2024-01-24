from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class PackageUpdateSchema(Schema):
    package_name = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))
    duration = fields.Str(required=True, validate=validate.Regexp(RegularExp.DURATION))
    category = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))
    price = fields.Str(required=True)
    status = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))

class PackageSchema(PackageUpdateSchema):
    package_id = fields.Str(dump_only=True)
    
class ItineraryUpdateSchema(Schema):
    day = fields.Int(required=True)
    city = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))
    description = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))

class ItinerarySchema(ItineraryUpdateSchema):
    itineray_id = fields.Str(dump_only=True)
    package_id = fields.Str(required=True)
    