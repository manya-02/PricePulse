from . import db


class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False, unique=True)

    website = db.Column(db.String(500))

    offers = db.relationship(
        "Offer",
        backref="platform",
        lazy=True
    )

    def __repr__(self):
        return f"<Platform {self.name}>"