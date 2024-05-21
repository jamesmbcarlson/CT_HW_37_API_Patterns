from flask import request, jsonify
from schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        # Validate and deserialize the request data
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Call the save service with the order data
    order_save = orderService.save(order_data)
    # Check to see that the order_save is a order and not None
    if order_save is not None:
        # Serialize the order data and return with a 201 success
        return order_schema.jsonify(order_save), 201
    else:
        return jsonify({"Message": "order_save is None"}), 400
    
@cache.cached(timeout=20)
def find_all():
    orders = orderService.find_all()
    return orders_schema.jsonify(orders), 200
    