from datetime import datetime

from .base_platform import BasePlatform


class MockPlatform(BasePlatform):

    def __init__(self, name):

        self.name = name

    def search_product(self, product_name):

        product_name_lower = product_name.lower()

        # --------------------------------------
        # iPhone 15 - 128GB
        # --------------------------------------

        if "iphone 15" in product_name_lower and "128gb" in product_name_lower:

            prices = {
                "Amazon": 52999,
                "Flipkart": 51499,
                "Blinkit": 54999,
                "Zepto": 53999
            }

        # --------------------------------------
        # iPhone 15 - 256GB
        # --------------------------------------

        elif "iphone 15" in product_name_lower and "256gb" in product_name_lower:

            prices = {
                "Amazon": 62999,
                "Flipkart": 61499,
                "Blinkit": 64999,
                "Zepto": 63999
            }

        # --------------------------------------
        # Samsung Galaxy S24 - 128GB
        # --------------------------------------

        elif "galaxy s24" in product_name_lower and "128gb" in product_name_lower:

            prices = {
                "Amazon": 55999,
                "Flipkart": 54499,
                "Blinkit": 57999,
                "Zepto": 56999
            }

        # --------------------------------------
        # Default price
        # --------------------------------------

        else:

            prices = {
                "Amazon": 50000,
                "Flipkart": 49000,
                "Blinkit": 52000,
                "Zepto": 51000
            }

        price = prices.get(
            self.name,
            50000
        )

        return [

            {
                "platform": self.name,

                "product_name": product_name,

                "price": price,

                "original_price": price + 2000,

                "availability": "Available",

                "product_url": "https://example.com",

                "last_updated": datetime.utcnow()
            }
        ]