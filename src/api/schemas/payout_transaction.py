from marshmallow import Schema, fields

class PayoutTransactionRequestSchema(Schema):
    recipient_id = fields.Int(required=True)
    recipient_type = fields.Str(required=True)
    amount = fields.Float(required=True)
    status = fields.Str(required=True)
    processed_by_admin_id = fields.Int(required=True)

class PayoutTransactionResponseSchema(Schema):
    transactions_id = fields.Int(required=True)
    recipient_id = fields.Int(required=True)
    recipient_type = fields.Str(required=True)
    amount = fields.Float(required=True)
    transaction_date = fields.Raw(required=True)
    status = fields.Str(required=True)
    processed_by_admin_id = fields.Int(required=True)