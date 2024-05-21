from flask import request, jsonify
from schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        # Validate and deserialize the request data
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Call the save service with the product data
    product_save = productService.save(product_data)
    # Check to see that the product_save is a product and not None
    if product_save is not None:
        # Serialize the product data and return with a 201 success
        return product_schema.jsonify(product_save), 201
    else:
        return jsonify({"Message": "product_save is None"}), 400
    
@cache.cached(timeout=20)
def find_all():
    products = productService.find_all()
    return products_schema.jsonify(products), 200
    