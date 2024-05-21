from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

# from models.order import Order
# from models.production import Production

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    # Many-to-Many Relationship with Order
    orders: Mapped[list['Order']] = db.relationship(back_populates='products')

    # One-to-Many Relationship with Production
    production: Mapped[list['Production']] = db.relationship(back_populates='product')
    