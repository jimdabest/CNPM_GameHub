from src.api.controllers.todo_controller import bp as todo_bp
from src.api.controllers.user_controller import bp as user_bp

def register_routes(app):
    app.register_blueprint(todo_bp) 
    app.register_blueprint(user_bp)