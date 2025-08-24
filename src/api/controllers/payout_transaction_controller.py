from flask import Blueprint, request, jsonify
from services.payout_transaction_service import PayoutTransactionService
from infrastructure.repositories.payout_transaction_repository import PayoutTransactionRepository
from api.schemas.payout_transaction import PayoutTransactionRequestSchema, PayoutTransactionResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('payout_transaction', __name__, url_prefix='/payout-transactions')

payout_transaction_service = PayoutTransactionService(PayoutTransactionRepository(session))

request_schema = PayoutTransactionRequestSchema()
response_schema = PayoutTransactionResponseSchema()

@bp.route('/', methods=['GET'])
def list_payout_transactions():
    """
    Get all payout transactions
    ---
    get:
      summary: Get all payout transactions
      tags:
        - Payout Transactions
      responses:
        200:
          description: List of payout transactions
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/PayoutTransactionResponse'
    """
    payout_transactions = payout_transaction_service.list_payout_transactions()
    return jsonify(response_schema.dump(payout_transactions, many=True)), 200

@bp.route('/<int:transaction_id>', methods=['GET'])
def get_payout_transaction(transaction_id):
    """
    Get payout transaction by id
    ---
    get:
      summary: Get payout transaction by id
      parameters:
        - name: transaction_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của payout transaction cần lấy
      tags:
        - Payout Transactions
      responses:
        200:
          description: object of payout transaction
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayoutTransactionResponse'
        404:
          description: Payout transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    payout_transaction = payout_transaction_service.get_payout_transaction(transaction_id)
    if not payout_transaction:
        return jsonify({'message': 'Payout transaction not found'}), 404
    return jsonify(response_schema.dump(payout_transaction)), 200

@bp.route('/', methods=['POST'])
def create_payout_transaction():
    """
    Create a new payout transaction
    ---
    post:
      summary: Create a new payout transaction
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PayoutTransactionRequest'
      tags:
        - Payout Transactions
      responses:
        201:
          description: Payout transaction created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayoutTransactionResponse'
        400:
          description: Invalid input
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    now = datetime.utcnow()
    payout_transaction = payout_transaction_service.create_payout_transaction(
        recipient_id=data['recipient_id'],
        recipient_type=data['recipient_type'],
        amount=data['amount'],
        transaction_date=now,
        status=data['status'],
        processed_by_admin_id=data['processed_by_admin_id']
    )
    return jsonify(response_schema.dump(payout_transaction)), 201

@bp.route('/<int:transaction_id>', methods=['PUT'])
def update_payout_transaction(transaction_id):
    """
    Update payout transaction
    ---
    put:
      summary: Update payout transaction by id
      parameters:
        - name: transaction_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của payout transaction cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PayoutTransactionRequest'
      tags:
        - Payout Transactions
      responses:
        200:
          description: Payout transaction updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayoutTransactionResponse'
        400:
          description: Invalid input
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        404:
          description: Payout transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    payout_transaction = payout_transaction_service.update_payout_transaction(
        transaction_id=transaction_id,
        recipient_id=data['recipient_id'],
        recipient_type=data['recipient_type'],
        amount=data['amount'],
        transaction_date=datetime.utcnow(),
        status=data['status'],
        processed_by_admin_id=data['processed_by_admin_id']
    )
    return jsonify(response_schema.dump(payout_transaction)), 200

@bp.route('/<int:transaction_id>', methods=['DELETE'])
def delete_payout_transaction(transaction_id):
    """
    Delete payout transaction
    ---
    delete:
      summary: Delete payout transaction by id
      parameters:
        - name: transaction_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của payout transaction cần xóa
      tags:
        - Payout Transactions
      responses:
        204:
          description: Payout transaction deleted successfully
        404:
          description: Payout transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    payout_transaction_service.delete_payout_transaction(transaction_id)
    return '', 204