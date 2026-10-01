from models import db
from models.platform import Platform
from models.offer import Offer


def save_offers(product, platform_offers):

    saved_offers = []

    for data in platform_offers:

        platform = Platform.query.filter_by(
            name=data["platform"]
        ).first()

        if not platform:

            platform = Platform(
                name=data["platform"],
                website=data.get("product_url")
            )

            db.session.add(platform)
            db.session.commit()

        offer = Offer.query.filter_by(
            product_id=product.id,
            platform_id=platform.id
        ).first()

        if offer:

            offer.price = data["price"]

            offer.original_price = data.get(
                "original_price"
            )

            offer.product_url = data.get(
                "product_url"
            )

            offer.image_url = data.get(
                "image_url"
            )

            offer.availability = data.get(
                "availability",
                "Available"
            )

            offer.last_updated = data.get(
                "last_updated"
            )

        else:

            offer = Offer(

                product_id=product.id,

                platform_id=platform.id,

                price=data["price"],

                original_price=data.get(
                    "original_price"
                ),

                product_url=data.get(
                    "product_url"
                ),

                image_url=data.get(
                    "image_url"
                ),

                availability=data.get(
                    "availability",
                    "Available"
                ),

                last_updated=data.get(
                    "last_updated"
                )
            )

            db.session.add(offer)

        saved_offers.append(offer)

    db.session.commit()

    return saved_offers