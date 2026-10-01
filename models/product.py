from . import db


class Product(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(200),
        nullable=False
    )

    brand = db.Column(
        db.String(100)
    )

    category = db.Column(
        db.String(100)
    )

    description = db.Column(
        db.Text
    )

    image_url = db.Column(
        db.String(500)
    )

    storage = db.Column(
        db.String(20)
    )

    model_number = db.Column(
        db.String(100)
    )

    color = db.Column(
        db.String(50)
    )

    offers = db.relationship(
        "Offer",
        backref="product",
        lazy=True
    )

    def __repr__(self):

        return f"<Product {self.name}>"