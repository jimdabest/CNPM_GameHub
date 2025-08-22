from flask import Blueprint, request, jsonify
from services.user_service import UserService
from infrastructure.repositories.user_repository import UserRepository
from api.schemas.user import UserRequestSchema, UserResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('user', __name__, url_prefix='/users')

user_service = UserService(UserRepository(session))

request_schema = UserRequestSchema()
response_schema = UserResponseSchema()

@bp.route('/', methods=['GET'])
def list_users():
    """
    Get all users
    ---
    get:
      summary: Get all users
      tags:
        - Users
      responses:
        200:
          description: List of users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/UserResponse'
    """
    users = user_service.list_users()
    return jsonify(response_schema.dump(users, many=True)), 200

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by id
    ---
    get:
      summary: Get user by id
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của người dùng cần lấy
      tags:
        - Users
      responses:
        200:
          description: object of user
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
        404:
          description: User not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    user = user_service.get_user_by_id(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(response_schema.dump(user)), 200

@bp.route('/', methods=['POST'])
def add_user():
    """
    Add a new user
    ---
    post:
      summary: Add a new user
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRequest'
      responses:
        201:
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
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
    user = user_service.add_user(
        username=data['username'],
        password=data['password'],
        role=data['role'],
        status=data['status'],
        created_at=now,
        updated_at=now
    )
    return jsonify(response_schema.dump(user)), 201  

@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update an existing user
    ---
    put:
      summary: Update an existing user
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của người dùng cần cập nhật
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRequest'
      responses:
        200:
          description: User updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
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
          description: User not found
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
    
    try:
        user = user_service.update_user(
            user_id=user_id,  # Fixed: use user_id parameter instead of id
            username=data['username'],
            password=data['password'],
            role=data['role'],
            status=data['status'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return jsonify(response_schema.dump(user)), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by id
    ---
    delete:
      summary: Delete a user by id
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của người dùng cần xóa
      tags:
        - Users
      responses:
        204:
          description: User deleted successfully
        404:
          description: User not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    try:
        user_service.delete_user(user_id)
        return '', 204
    except ValueError as e:
        return jsonify({'message': str(e)}), 404