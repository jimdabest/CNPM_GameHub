from marshmallow import Schema, fields
from datetime import datetime

class AdminRequestSchema(Schema):
    user_id = fields.Int(required=True)

class AdminResponseSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)