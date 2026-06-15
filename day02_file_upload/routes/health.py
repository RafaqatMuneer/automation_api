from flask import Blueprint
from utils.response import success_response

health_bp = Blueprint('health_check',__name__)

@health_bp.route("/health", methods = ["GET"])
def health_check():
    """App-level health check."""
    return success_response(message="Server is running")