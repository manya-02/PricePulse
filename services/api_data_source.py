import time

import requests

from services.http_client import HTTPClient

from services.api_config import (
    get_platform_config
)

from services.api_response_parser import (
    parse_product_response
)

from services.api_response_handler import (
    get_json_response
)

from services.logger import get_logger

from config import Config


logger = get_logger(
    "ApiDataSource"
)


class ApiDataSource:

    def __init__(self):

        self.http_client = HTTPClient(
            timeout=10
        )

    def should_retry_http_error(
        self,
        error
    ):
        """
        Decide whether an HTTP error is
        temporary and should be retried.
        """

        response = getattr(
            error,
            "response",
            None
        )

        if response is None:

            return False

        status_code = (
            response.status_code
        )

        # 429 = Too Many Requests

        if status_code == 429:

            return True

        # 5xx = temporary server errors

        if 500 <= status_code <= 599:

            return True

        return False

    def get_retry_delay(
        self,
        attempt
    ):
        """
        Calculate exponential backoff delay.

        Attempt 1 -> base delay
        Attempt 2 -> base delay * 2
        Attempt 3 -> base delay * 4

        Maximum delay is limited to 10 seconds.
        """

        base_delay = max(
            0,
            Config.API_RETRY_DELAY
        )

        delay = (
            base_delay
            * (2 ** (attempt - 1))
        )

        # Prevent excessively long waits

        max_delay = 10

        delay = min(
            delay,
            max_delay
        )

        return delay

    def search_product(
        self,
        platform_name,
        product_name
    ):

        platform_config = (
            get_platform_config(
                platform_name
            )
        )

        if not platform_config:

            raise ValueError(
                f"No API configuration found "
                f"for {platform_name}"
            )

        api_url = platform_config.get(
            "url"
        )

        if not api_url:

            raise ValueError(
                f"No API URL configured for "
                f"{platform_name}"
            )

        api_key = platform_config.get(
            "api_key",
            ""
        )

        query_parameter = (
            platform_config.get(
                "query_parameter",
                "q"
            )
        )

        auth_type = (
            platform_config.get(
                "auth_type",
                "bearer"
            )
        )

        params = {
            query_parameter:
                product_name
        }

        headers = {
            "Accept":
                "application/json"
        }

        if api_key:

            if auth_type == "bearer":

                headers["Authorization"] = (
                    f"Bearer {api_key}"
                )

            elif auth_type == "header":

                api_key_header = (
                    platform_config.get(
                        "api_key_header",
                        "X-API-Key"
                    )
                )

                headers[
                    api_key_header
                ] = api_key

        retry_count = max(
            0,
            Config.API_RETRY_COUNT
        )

        total_attempts = (
            retry_count + 1
        )

        for attempt in range(
            1,
            total_attempts + 1
        ):

            logger.info(
                f"API request attempt "
                f"{attempt}/{total_attempts} "
                f"for {platform_name}"
            )

            try:

                response = (
                    self.http_client.get(
                        api_url,
                        params=params,
                        headers=headers
                    )
                )

                data = get_json_response(
                    response
                )

                offers = (
                    parse_product_response(
                        platform_name,
                        data
                    )
                )

                logger.info(
                    f"{platform_name} API "
                    f"returned "
                    f"{len(offers)} offer(s)"
                )

                return offers

            except (
                TimeoutError,
                ConnectionError
            ) as error:

                if attempt >= total_attempts:

                    logger.error(
                        f"{platform_name} API "
                        f"failed after "
                        f"{attempt} attempts: "
                        f"{error}"
                    )

                    raise

                delay = self.get_retry_delay(
                    attempt
                )

                logger.warning(
                    f"{platform_name} API "
                    f"temporary network error. "
                    f"Retrying in "
                    f"{delay} second(s)..."
                )

                time.sleep(
                    delay
                )

            except requests.HTTPError as error:

                should_retry = (
                    self.should_retry_http_error(
                        error
                    )
                )

                if (
                    should_retry
                    and
                    attempt < total_attempts
                ):

                    delay = (
                        self.get_retry_delay(
                            attempt
                        )
                    )

                    logger.warning(
                        f"{platform_name} API "
                        f"returned a temporary "
                        f"HTTP error. "
                        f"Retrying in "
                        f"{delay} second(s)..."
                    )

                    time.sleep(
                        delay
                    )

                    continue

                logger.error(
                    f"{platform_name} API "
                    f"HTTP request failed: "
                    f"{error}"
                )

                raise

            except ValueError as error:

                logger.error(
                    f"{platform_name} API "
                    f"response error: "
                    f"{error}"
                )

                raise