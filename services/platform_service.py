from datetime import datetime


def get_test_prices(product_name):
    """
    Temporary platform data.

    This is only for development.
    It does not represent live platform prices.
    """

    return [
        {
            "platform": "Amazon",
            "price": 52999,
            "original_price": 54999,
            "availability": "Available",
            "product_url": "https://www.amazon.in",
            "last_updated": datetime.utcnow()
        },

        {
            "platform": "Flipkart",
            "price": 51499,
            "original_price": 54999,
            "availability": "Available",
            "product_url": "https://www.flipkart.com",
            "last_updated": datetime.utcnow()
        },

        {
            "platform": "Blinkit",
            "price": 54999,
            "original_price": 54999,
            "availability": "Available",
            "product_url": "https://blinkit.com",
            "last_updated": datetime.utcnow()
        },

        {
            "platform": "Zepto",
            "price": 53999,
            "original_price": 54999,
            "availability": "Available",
            "product_url": "https://www.zeptonow.com",
            "last_updated": datetime.utcnow()
        }
    ]