from datetime import datetime


REQUIRED_FIELDS = [
    "platform",
    "product_name",
    "price",
    "availability"
]


def validate_offer(offer):

    # ----------------------------------
    # Check that offer is a dictionary
    # ----------------------------------

    if not isinstance(offer, dict):

        return False, "Offer must be a dictionary"

    # ----------------------------------
    # Check required fields
    # ----------------------------------

    for field in REQUIRED_FIELDS:

        if field not in offer:

            return False, (
                f"Missing required field: {field}"
            )

    # ----------------------------------
    # Validate platform
    # ----------------------------------

    if not isinstance(
        offer["platform"],
        str
    ):

        return False, (
            "Platform must be a string"
        )

    if not offer["platform"].strip():

        return False, (
            "Platform cannot be empty"
        )

    # ----------------------------------
    # Validate product name
    # ----------------------------------

    if not isinstance(
        offer["product_name"],
        str
    ):

        return False, (
            "Product name must be a string"
        )

    if not offer["product_name"].strip():

        return False, (
            "Product name cannot be empty"
        )

    # ----------------------------------
    # Validate price
    # ----------------------------------

    try:

        price = float(
            offer["price"]
        )

    except (
        TypeError,
        ValueError
    ):

        return False, (
            "Price must be a number"
        )

    if price <= 0:

        return False, (
            "Price must be greater than zero"
        )

    # ----------------------------------
    # Validate original price
    # ----------------------------------

    if offer.get("original_price") is not None:

        try:

            original_price = float(
                offer["original_price"]
            )

        except (
            TypeError,
            ValueError
        ):

            return False, (
                "Original price must be a number"
            )

        if original_price <= 0:

            return False, (
                "Original price must be greater than zero"
            )

    # ----------------------------------
    # Validate availability
    # ----------------------------------

    if not isinstance(
        offer["availability"],
        str
    ):

        return False, (
            "Availability must be a string"
        )

    # ----------------------------------
    # Validate timestamp
    # ----------------------------------

    if offer.get("last_updated") is not None:

        if not isinstance(
            offer["last_updated"],
            datetime
        ):

            return False, (
                "last_updated must be a datetime"
            )

    return True, None