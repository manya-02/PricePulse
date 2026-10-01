from .data_source import DataSource
from .platform_response import create_offer


class MockDataSource(DataSource):

    def search_product(
        self,
        platform_name,
        product_name
    ):

        product_name_lower = (
            product_name.lower()
        )

        # ----------------------------------
        # iPhone 15 - 128GB
        # ----------------------------------

        if (
            "iphone 15" in product_name_lower
            and "128gb" in product_name_lower
        ):

            prices = {

                "Amazon": 52999,

                "Flipkart": 51499,

                "Blinkit": 54999,

                "Zepto": 53999

            }

        # ----------------------------------
        # iPhone 15 - 256GB
        # ----------------------------------

        elif (
            "iphone 15" in product_name_lower
            and "256gb" in product_name_lower
        ):

            prices = {

                "Amazon": 62999,

                "Flipkart": 61499,

                "Blinkit": 64999,

                "Zepto": 63999

            }

        # ----------------------------------
        # Galaxy S24 - 128GB
        # ----------------------------------

        elif (
            "galaxy s24" in product_name_lower
            and "128gb" in product_name_lower
        ):

            prices = {

                "Amazon": 55999,

                "Flipkart": 54499,

                "Blinkit": 57999,

                "Zepto": 56999

            }

        # ----------------------------------
        # Default development price
        # ----------------------------------

        else:

            prices = {

                "Amazon": 50000,

                "Flipkart": 49000,

                "Blinkit": 52000,

                "Zepto": 51000

            }

        price = prices.get(
            platform_name,
            50000
        )

        return [

            create_offer(

                platform=platform_name,

                product_name=product_name,

                price=price,

                original_price=price + 2000,

                availability="Available",

                product_url=None,

                image_url=None

            )

        ]