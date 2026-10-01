from config import Config

from .amazon_platform import (
    AmazonPlatform
)

from .flipkart_platform import (
    FlipkartPlatform
)

from .blinkit_platform import (
    BlinkitPlatform
)

from .zepto_platform import (
    ZeptoPlatform
)


def get_platform_source():

    data_source = (
        Config.DATA_SOURCE
        or "mock"
    )

    return (
        data_source
        .strip()
        .lower()
    )


def create_platforms():

    data_source = (
        get_platform_source()
    )

    # ----------------------------------
    # Supported data sources
    # ----------------------------------

    if data_source in [
        "mock",
        "api"
    ]:

        return [
            AmazonPlatform(),
            FlipkartPlatform(),
            BlinkitPlatform(),
            ZeptoPlatform()
        ]

    # ----------------------------------
    # Invalid configuration
    # ----------------------------------

    raise ValueError(
        f"Unsupported DATA_SOURCE: "
        f"'{data_source}'. "
        f"Use 'mock' or 'api'."
    )