import time

from .platform_result import create_platform_error
from .logger import get_logger


logger = get_logger(
    "PlatformManager"
)


class PlatformManager:

    def __init__(self, platforms):

        self.platforms = platforms

    def search_platform(
        self,
        platform,
        product_name
    ):

        start_time = time.perf_counter()

        try:

            logger.info(
                f"Searching {platform.name}"
            )

            offers = platform.search_product(
                product_name
            )

            elapsed_time = (
                time.perf_counter()
                - start_time
            )

            elapsed_time = round(
                elapsed_time,
                3
            )

            if offers:

                logger.info(
                    f"{platform.name} "
                    f"returned "
                    f"{len(offers)} offer(s) "
                    f"in "
                    f"{elapsed_time}s"
                )

                return offers

            logger.warning(
                f"{platform.name} "
                f"returned no results "
                f"in "
                f"{elapsed_time}s"
            )

            return [
                create_platform_error(
                    platform.name,
                    "No results found"
                )
            ]

        except TimeoutError:

            elapsed_time = (
                time.perf_counter()
                - start_time
            )

            elapsed_time = round(
                elapsed_time,
                3
            )

            logger.error(
                f"{platform.name} "
                f"timed out after "
                f"{elapsed_time}s"
            )

            return [
                create_platform_error(
                    platform.name,
                    "Request timed out"
                )
            ]

        except Exception as error:

            elapsed_time = (
                time.perf_counter()
                - start_time
            )

            elapsed_time = round(
                elapsed_time,
                3
            )

            logger.exception(
                f"{platform.name} "
                f"failed after "
                f"{elapsed_time}s: "
                f"{error}"
            )

            return [
                create_platform_error(
                    platform.name,
                    str(error)
                )
            ]

    def search_all(
        self,
        product_name
    ):

        all_offers = []

        overall_start = time.perf_counter()

        logger.info(
            f"Searching all platforms for: "
            f"{product_name}"
        )

        for platform in self.platforms:

            offers = self.search_platform(
                platform,
                product_name
            )

            all_offers.extend(
                offers
            )

        overall_time = (
            time.perf_counter()
            - overall_start
        )

        overall_time = round(
            overall_time,
            3
        )

        logger.info(
            f"All platform searches "
            f"completed in "
            f"{overall_time}s"
        )

        return all_offers