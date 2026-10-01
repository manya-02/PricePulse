import os

from dotenv import load_dotenv


load_dotenv()


class Config:

    # ----------------------------------
    # Flask
    # ----------------------------------

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key"
    )

    # ----------------------------------
    # Database
    # ----------------------------------

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///pricepulse.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ----------------------------------
    # Data Source
    # ----------------------------------

    DATA_SOURCE = os.getenv(
        "DATA_SOURCE",
        "mock"
    )

    # ----------------------------------
    # Cache
    # ----------------------------------

    PRICE_CACHE_MINUTES = int(
        os.getenv(
            "PRICE_CACHE_MINUTES",
            "10"
        )
    )

    # ----------------------------------
    # API Keys
    # ----------------------------------

    AMAZON_API_KEY = os.getenv(
        "AMAZON_API_KEY",
        ""
    )

    FLIPKART_API_KEY = os.getenv(
        "FLIPKART_API_KEY",
        ""
    )

    BLINKIT_API_KEY = os.getenv(
        "BLINKIT_API_KEY",
        ""
    )

    ZEPTO_API_KEY = os.getenv(
        "ZEPTO_API_KEY",
        ""
    )

    AMAZON_API_URL = os.getenv(
        "AMAZON_API_URL",
        ""
    )

    FLIPKART_API_URL = os.getenv(
        "FLIPKART_API_URL",
        ""
    )

    BLINKIT_API_URL = os.getenv(
        "BLINKIT_API_URL",
        ""
    )

    ZEPTO_API_URL = os.getenv(
        "ZEPTO_API_URL",
        ""
    )

    API_RETRY_COUNT = int(
        os.getenv(
            "API_RETRY_COUNT",
            "2"
        )
    )

    API_RETRY_DELAY = float(
        os.getenv(
            "API_RETRY_DELAY",
            "1"
        )
    )