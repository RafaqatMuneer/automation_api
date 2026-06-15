from flask import Blueprint
from utils.response import success_response, error_response
# BLueprint name = products, for internal routing
products_bp = Blueprint('products',__name__)

@products_bp.route('/products',methods = ['GET'])
def get_products():
    """Return Full list of products"""
    products = [
        {"id": 1, "name": "Laptop",  "price": 85000, "in_stock": True},
        {"id": 2, "name": "Mouse",   "price": 1500,  "in_stock": True},
        {"id": 3, "name": "Monitor", "price": 32000, "in_stock": False}
    ]
    return success_response(
        data=products,
        message="Products fetched successfully"
    )
@products_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Return a single searched product"""
    products = [
        {"id": 1, "name": "Laptop",  "price": 85000, "in_stock": True},
        {"id": 2, "name": "Mouse",   "price": 1500,  "in_stock": True},
        {"id": 3, "name": "Monitor", "price": 32000, "in_stock": False}
    ]
    # Serach for the product
    product = next((p for p in products if p['id'] == product_id), None)

    if product is None:
        return error_response(
            message=f"Product with id {product_id} is not found",
            status_code= 404
        )
    return success_response(
        data=product,
        message="Product fetched successfully"
    )
@products_bp.route("/health", methods = ["GET"])
def health_check():
    """Quick check that server is alive"""
    return success_response(message="Server is running")
"""Adding route for categories"""
@products_bp.route("/categories", methods = ['GET'])
def get_categories():
    categories = [
        {'id' : 1, 'name':'electronics'},
        {'id': 2, 'name':'cloths'},
        {'id':3, 'name': 'sports' }
    ]
    return success_response(
        data=categories,
        message="Categories fetched successfully"
    )