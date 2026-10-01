from config import Config

from .mock_data_source import (
    MockDataSource
)

from .api_data_source import (
    ApiDataSource
)


def get_data_source_name():

    data_source = (
        Config.DATA_SOURCE
        or "mock"
    )

    data_source = (
        data_source
        .strip()
        .lower()
    )

    if not data_source:

        data_source = "mock"

    return data_source


def create_data_source():

    data_source = (
        get_data_source_name()
    )

    # ----------------------------------
    # Mock data source
    # ----------------------------------

    if data_source == "mock":

        return MockDataSource()

    # ----------------------------------
    # API data source
    # ----------------------------------

    if data_source == "api":

        return ApiDataSource()

    # ----------------------------------
    # Invalid data source
    # ----------------------------------

    raise ValueError(
        f"Unsupported DATA_SOURCE: "
        f"'{data_source}'. "
        f"Use 'mock' or 'api'."
    )