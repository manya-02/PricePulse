from services.platform_response import create_offer


def normalize_product_response(
    platform,
    data
):
    """
    Convert a raw product response into
    the standard PricePulse offer format.
    """

    if not isinstance(data, dict):

        return None

    # ----------------------------------
    # Product name
    # ----------------------------------

    product_name = (
        data.get("product_name")
        or data.get("name")
        or data.get("title")
    )

    # ----------------------------------
    # Price
    # ----------------------------------

    price = (
        data.get("price")
        or data.get("selling_price")
        or data.get("sale_price")
    )

    # ----------------------------------
    # Original price
    # ----------------------------------

    original_price = (
        data.get("original_price")
        or data.get("mrp")
        or data.get("list_price")
    )

    # ----------------------------------
    # Availability
    # ----------------------------------

    availability = (
        data.get("availability")
        or data.get("stock_status")
        or data.get("status")
        or "Available"
    )

    # ----------------------------------
    # Product URL
    # ----------------------------------

    product_url = (
        data.get("product_url")
        or data.get("url")
        or data.get("link")
    )

    # ----------------------------------
    # Product image
    # ----------------------------------

    image_url = (
        data.get("image_url")
        or data.get("image")
        or data.get("thumbnail")
    )

    # ----------------------------------
    # Required data check
    # ----------------------------------

    if not product_name:

        return None

    if price is None:

        return None

    # ----------------------------------
    # Create standard offer
    # ----------------------------------

    return create_offer(

        platform=platform,

        product_name=product_name,

        price=price,

        original_price=original_price,

        availability=availability,

        product_url=product_url,

        image_url=image_url

    )


def normalize_product_list(
    platform,
    data
):
    """
    Convert a list of raw product responses
    into standard PricePulse offers.
    """

    if not isinstance(data, list):

        return []

    offers = []

    for item in data:

        offer = normalize_product_response(
            platform,
            item
        )

        if offer:

            offers.append(
                offer
            )

    return offers