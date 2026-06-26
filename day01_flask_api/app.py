from flask import Flask
from config import Config
from utils.response import error_response
from routes.products import products_bp


def create_app():
    """Create app methods to avoid messy data
    sequence would be:
    -create Flask object
    -Register Blueprints
    -Return app
    """
    """
    Application factory function.
    Creates and configures the Flask app.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    #Register Blueprint
    app.register_blueprint(products_bp, url_prefix='/api')

    #Global error Handlers
    @app.errorhandler(404)
    def not_found(e):
        return error_response(
            message="The resource you are looking for is not found",
            status_code=404
        )
    #Global 405 handler
    @app.errorhandler(405)
    def method_not_allowed(e):
        return error_response(
            message="HTTP mehtod not allowed on this route",
            status_code=405
        )
    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug = Config.DEBUG)