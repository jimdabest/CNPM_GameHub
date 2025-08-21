from flask import Blueprint, request, jsonify
from services.designer_service import DesignerService
from infrastructure.repositories.designer_repository import DesignerRepository
from api.schemas.designer import DesignerRequestSchema, DesignerResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('designer', __name__, url_prefix='/designers')


designer_service = DesignerService(DesignerRepository(session))

request_schema = DesignerRequestSchema()
response_schema = DesignerResponseSchema()

@bp.route('/', methods=['GET'])
def list_designers():
    """
    Get all designers
    ---
    get:
      summary: Get all designers
      tags:
        - Designers
      responses:
        200:
          description: List of designers
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/DesignerResponse'
    """
    designers = designer_service.list_designers()
    return jsonify(response_schema.dump(designers, many=True)), 200


@bp.route('/<int:designer_id>', methods=['GET'])
def get_designer(designer_id):
    """
    Get designer by id
    ---
    get:
      summary: Get designer by id
      parameters:
        - name: designer_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của designer cần lấy
      tags:
        - Designers
      responses:
        200:
          description: object of designer
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DesignerResponse'
        404:
          description: Designer not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    designer = designer_service.get_designer(designer_id)
    if not designer:
        return jsonify({'message': 'Designer not found'}), 404
    return jsonify(response_schema.dump(designer)), 200


@bp.route('/', methods=['POST'])
def create_designer():
    """
    Create a new designer
    ---
    post:
      summary: Create a new designer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DesignerRequest'
      tags:
        - Designers
      responses:
        201:
          description: Designer created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DesignerResponse'
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

    # Tuỳ schema/service: bổ sung các trường khác nếu có (vd: status)
    designer = designer_service.create_designer(
        user_id=data['user_id'],
        paymentinfo=data.get('paymentinfo'),
        # Ví dụ nếu schema có 'status': status=data.get('status'),
        # Ví dụ nếu cần timestamps: created_at=datetime.utcnow(), updated_at=datetime.utcnow()
    )
    return jsonify(response_schema.dump(designer)), 201


@bp.route('/<int:designer_id>', methods=['PUT'])
def update_designer(designer_id):
    """
    Update a designer by id
    ---
    put:
      summary: Update a designer by id
      parameters:
        - name: designer_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của designer cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DesignerRequest'
      tags:
        - Designers
      responses:
        200:
          description: Designer updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DesignerResponse'
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
          description: Designer not found
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

    designer = designer_service.update_designer(
        designer_id=designer_id,
        user_id=data['user_id'],
        paymentinfo=data.get('paymentinfo'),
        # Ví dụ nếu schema có 'status': status=data.get('status'),
        # Ví dụ nếu cần timestamp cập nhật: updated_at=datetime.utcnow()
    )
    if not designer:
        return jsonify({'message': 'Designer not found'}), 404

    return jsonify(response_schema.dump(designer)), 200


@bp.route('/<int:designer_id>', methods=['DELETE'])
def delete_designer(designer_id):
    """
    Delete a designer by id
    ---
    delete:
      summary: Delete a designer by id
      parameters:
        - name: designer_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của designer cần xóa
      tags:
        - Designers
      responses:
        204:
          description: Designer deleted successfully
        404:
          description: Designer not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    deleted = designer_service.delete_designer(designer_id)
    if not deleted:
        return jsonify({'message': 'Designer not found'}), 404
    return '', 204
