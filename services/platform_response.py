from datetime import datetime


def create_offer(
    platform,
    product_name,
    price,
    original_price=None,
    availability="Available",
    product_url=None,
    image_url=None
):

    return {

        "platform": platform,

        "product_name": product_name,

        "price": float(price),

        "original_price": (
            float(original_price)
            if original_price is not None
            else None
        ),

        "availability": availability,

        "product_url": product_url,

        "image_url": image_url,

        "last_updated": datetime.utcnow()
    }