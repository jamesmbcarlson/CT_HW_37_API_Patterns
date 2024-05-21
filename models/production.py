from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

# from models.product import Product

class Production(Base):
    __tablename__ = "production"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'), nullable=False)
    quantity_produced: Mapped[int] = mapped_column(nullable=False)
    date_produced: Mapped[str] = mapped_column(db.Date, nullable=False)

    # Many-to-One Relationship with Customer
    product: Mapped['Product'] = db.relationship(back_populates='production')