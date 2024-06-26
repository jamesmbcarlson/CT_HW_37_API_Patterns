from sqlalchemy.orm import Session
from database import db
from models.product import Product

# Creates new product
def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(
                name=product_data['name'], 
                price=product_data['price'])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product
    
    
# Get all products in database
def find_all():
    query = db.select(Product)
    products = db.session.execute(query).scalars().all()
    return products