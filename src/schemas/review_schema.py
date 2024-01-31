from marshmallow import Schema, fields, validate
from config.regex_value import RegularExp

class GetReviewSchema(Schema):
    name = fields.Str(dump_only=True)
    comment = fields.Str(dump_only=True)
    date = fields.Str(dump_only=True)

class PostReviewSchema(Schema):
    booking_id = fields.Str(required=True, validate=validate.Regexp(RegularExp.UUID))
    name = fields.String(required=True, validate=validate.Regexp(RegularExp.NAME))
    comment = fields.Str(required=True, validate=validate.Regexp(RegularExp.STRING_VALUE))


