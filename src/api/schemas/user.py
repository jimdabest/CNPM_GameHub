from marshmallow import Schema, fields

class UserRequestSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str(required=True)
    status = fields.Boolean(required=True)
class UserResponseSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    password = fields.String(required=True)
    role = fields.Str(required=True)
    status = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)