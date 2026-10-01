from config import Config


API_CONFIG = {

    "Amazon": {
        "url": Config.AMAZON_API_URL,
        "api_key": Config.AMAZON_API_KEY,
        "query_parameter": "q",
        "auth_type": "bearer",
        "api_key_header": "Authorization"
    },

    "Flipkart": {
        "url": Config.FLIPKART_API_URL,
        "api_key": Config.FLIPKART_API_KEY,
        "query_parameter": "q",
        "auth_type": "bearer",
        "api_key_header": "Authorization"
    },

    "Blinkit": {
        "url": Config.BLINKIT_API_URL,
        "api_key": Config.BLINKIT_API_KEY,
        "query_parameter": "q",
        "auth_type": "bearer",
        "api_key_header": "Authorization"
    },

    "Zepto": {
        "url": Config.ZEPTO_API_URL,
        "api_key": Config.ZEPTO_API_KEY,
        "query_parameter": "q",
        "auth_type": "bearer",
        "api_key_header": "Authorization"
    }
}


def get_platform_config(
    platform_name
):

    return API_CONFIG.get(
        platform_name
    )


def get_api_key(
    platform_name
):

    config = get_platform_config(
        platform_name
    )

    if not config:
        return ""

    return config.get(
        "api_key",
        ""
    )


def get_api_url(
    platform_name
):

    config = get_platform_config(
        platform_name
    )

    if not config:
        return ""

    return config.get(
        "url",
        ""
    )