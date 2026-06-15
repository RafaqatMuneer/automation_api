from flask import Flask
from config import Config
from utils.response import success_response, error_response
from routes.uploads import uploads_bp
from routes.health import health_bp
from routes.products import products_bp

def create_app():

    """Application factory — registers all blueprints and error handlers."""
    app = Flask(__name__)
    app.config.from_object(Config)
    # Register Blueprints

    app.register_blueprint(uploads_bp, url_prefix='/api')
    app.register_blueprint(health_bp, url_prefix = '/api')
    app.register_blueprint(products_bp, url_prefix = '/api')


    # Global error handlers
    @app.errorhandler(404)
    def not_found(e):
        return error_response(
            message = "The speciefied resource does not exist",
            status_code=404
        )
    @app.errorhandler(405)
    def method_not_allowed(e):
        return error_response(
            message="HTTP method not allowed on this route",
            status_code=405
        )
    @app.errorhandler(413)
    def file_too_larger(e):
        return error_response(
            message="File size exceeded max allowed size of 2MB",
            status_code=413
        )
    @app.errorhandler(500)
    def file_not_found(e):
        return error_response(
            message="File not found",
            status_code=500
        )
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=Config.DEBUG)