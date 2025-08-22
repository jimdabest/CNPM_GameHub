from src.api.controllers.todo_controller import bp as todo_bp
from src.api.controllers.user_controller import bp as user_bp
from src.api.controllers.designer_controller import bp as designer_bp
from src.api.controllers.developer_controller import bp as developer_bp
from src.api.controllers.asset_purchases_controller import bp as asset_purchases_bp
from src.api.controllers.asset_controller import bp as asset_bp
from src.api.controllers.apiaccess_controller import bp as apiaccess_bp



def register_routes(app):
    app.register_blueprint(todo_bp) 
    app.register_blueprint(user_bp)
    app.register_blueprint(designer_bp)
    app.register_blueprint(developer_bp)
    app.register_blueprint(asset_purchases_bp)
    app.register_blueprint(asset_bp)
    app.register_blueprint(apiaccess_bp)



  