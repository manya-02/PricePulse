import requests

from services.logger import get_logger


logger = get_logger(
    "HTTPClient"
)


class HTTPClient:

    def __init__(
        self,
        timeout=10
    ):

        self.timeout = timeout

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent":
                "PricePulse/1.0",

            "Accept":
                "application/json"

        })

    def get(
        self,
        url,
        params=None,
        headers=None
    ):

        logger.info(
            f"GET request: {url}"
        )

        try:

            response = self.session.get(

                url,

                params=params,

                headers=headers,

                timeout=self.timeout

            )

            logger.info(

                f"Response received: "
                f"{response.status_code} "
                f"from {url}"

            )

            response.raise_for_status()

            return response

        except requests.Timeout:

            logger.error(

                f"Request timed out: "
                f"{url}"

            )

            raise TimeoutError(
                f"Request timed out: {url}"
            )

        except requests.ConnectionError:

            logger.error(

                f"Connection error: "
                f"{url}"

            )

            raise ConnectionError(
                f"Could not connect to: {url}"
            )

        except requests.HTTPError as error:

            logger.error(

                f"HTTP error for {url}: "
                f"{error}"

            )

            raise

        except requests.RequestException as error:

            logger.error(

                f"Request failed for {url}: "
                f"{error}"

            )

            raise