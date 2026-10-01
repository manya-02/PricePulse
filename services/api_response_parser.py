from services.response_normalizer import (
    normalize_product_response,
    normalize_product_list
)


def parse_product_response(
    platform,
    data
):

    if isinstance(data, dict):

        if (
            "price" in data
            or "selling_price" in data
            or "sale_price" in data
        ):

            offer = normalize_product_response(
                platform,
                data
            )

            if offer:

                return [offer]

            return []

        products = (
            data.get("products")
            or data.get("results")
            or data.get("items")
        )

        if isinstance(
            products,
            list
        ):

            return normalize_product_list(
                platform,
                products
            )

        return []

    if isinstance(data, list):

        return normalize_product_list(
            platform,
            data
        )

    return []