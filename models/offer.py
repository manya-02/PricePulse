from models import db
from datetime import datetime


class Offer(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id"),
        nullable=False
    )

    platform_id = db.Column(
        db.Integer,
        db.ForeignKey("platform.id"),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    original_price = db.Column(
        db.Float
    )

    product_url = db.Column(
        db.String(500)
    )

    image_url = db.Column(
        db.String(500)
    )

    availability = db.Column(
        db.String(50),
        default="Available"
    )

    last_updated = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Offer {self.price}>"