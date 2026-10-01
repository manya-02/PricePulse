def create_platform_error(
    platform,
    error_message
):

    return {
        "platform": platform,
        "product_name": None,
        "price": None,
        "original_price": None,
        "availability": "Unavailable",
        "product_url": None,
        "image_url": None,
        "last_updated": None,
        "error": error_message
    }