from marshmallow import Schema, fields

class AssetPurchaseRequestSchema(Schema):
    asset_name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)
    purchased_at = fields.DateTime(required=True)

class AssetPurchaseResponseSchema(Schema):
    id = fields.Int(required=True)
    asset_name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)
    purchased_at = fields.DateTime(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
