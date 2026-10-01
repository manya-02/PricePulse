import requests

from services.logger import get_logger


logger = get_logger(
    "ApiResponseHandler"
)


def get_json_response(response):
    """
    Safely convert an HTTP response into JSON.
    """

    # ----------------------------------
    # Check HTTP status
    # ----------------------------------

    if response.status_code >= 400:

        logger.error(
            f"API returned HTTP "
            f"{response.status_code}"
        )

        error = requests.HTTPError(
            f"API returned HTTP "
            f"{response.status_code}"
        )

        error.response = response

        raise error

    # ----------------------------------
    # Check empty response
    # ----------------------------------

    if not response.text.strip():

        logger.error(
            "API returned an empty response"
        )

        raise ValueError(
            "API returned an empty response"
        )

    # ----------------------------------
    # Convert to JSON
    # ----------------------------------

    try:

        data = response.json()

    except ValueError:

        logger.error(
            "API returned invalid JSON"
        )

        raise ValueError(
            "API returned invalid JSON"
        )

    # ----------------------------------
    # Check response type
    # ----------------------------------

    if not isinstance(
        data,
        (dict, list)
    ):

        logger.error(
            "API returned an unsupported "
            "response format"
        )

        raise ValueError(
            "API returned an unsupported "
            "response format"
        )

    return data