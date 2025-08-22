from marshmallow import Schema, fields

class DeveloperRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    skills = fields.List(fields.Str(), required=True)
    status = fields.Str(required=True)

class DeveloperResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    skills = fields.List(fields.Str(), required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
