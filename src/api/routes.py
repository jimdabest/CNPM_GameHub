from src.api.controllers.todo_controller import bp as todo_bp
from src.api.controllers.user_controller import bp as user_bp
from src.api.controllers.designer_controller import bp as designer_bp


def register_routes(app):
    app.register_blueprint(todo_bp) 
    app.register_blueprint(user_bp)
    app.register_blueprint(designer_bp)
  