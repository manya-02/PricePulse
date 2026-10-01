from services.offer_service import save_offers

from services.cache_service import (
    is_offer_fresh
)

from services.offer_validator import (
    validate_offer
)

from services.logger import get_logger


logger = get_logger(
    "PriceService"
)


def get_product_search_name(product):

    search_name = product.name

    if product.storage:

        search_name += (
            " "
            + product.storage
        )

    if product.color:

        search_name += (
            " "
            + product.color
        )

    return search_name


def get_product_offers(
    product,
    platform_manager
):

    existing_offers = list(
        product.offers
    )

    existing_by_platform = {}

    for offer in existing_offers:

        platform_name = (
            offer.platform.name
        )

        existing_by_platform[
            platform_name
        ] = offer

    search_name = get_product_search_name(
        product
    )

    logger.info(
        f"Getting offers for: "
        f"{search_name}"
    )

    for platform in platform_manager.platforms:

        existing_offer = (
            existing_by_platform.get(
                platform.name
            )
        )

        # ----------------------------------
        # USE CACHE
        # ----------------------------------

        if (
            existing_offer
            and
            is_offer_fresh(
                existing_offer
            )
        ):

            logger.info(
                f"Using cached offer for "
                f"{platform.name}"
            )

            continue

        # ----------------------------------
        # REFRESH PLATFORM
        # ----------------------------------

        if existing_offer:

            logger.info(
                f"Cached offer expired for "
                f"{platform.name}"
            )

        else:

            logger.info(
                f"No cached offer for "
                f"{platform.name}"
            )

        offers = (
            platform_manager.search_platform(
                platform,
                search_name
            )
        )

        # ----------------------------------
        # VALIDATE OFFERS
        # ----------------------------------

        valid_offers = []

        for offer in offers:

            is_valid, error_message = (
                validate_offer(offer)
            )

            if is_valid:

                valid_offers.append(
                    offer
                )

            else:

                logger.warning(

                    f"Invalid offer from "
                    f"{platform.name}: "
                    f"{error_message}"

                )

        # ----------------------------------
        # SAVE VALID OFFERS
        # ----------------------------------

        if valid_offers:

            save_offers(
                product,
                valid_offers
            )

            logger.info(
                f"Saved "
                f"{len(valid_offers)} "
                f"offer(s) from "
                f"{platform.name}"
            )

        else:

            logger.warning(
                f"No valid offers "
                f"received from "
                f"{platform.name}"
            )

    return list(
        product.offers
    )