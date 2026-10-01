from flask import (
    Blueprint,
    request,
    jsonify,
    render_template
)

from models.product import Product

from services.product_service import find_matching_products

from services.platform_manager import PlatformManager

from services.platform_factory import create_platforms

from services.price_service import get_product_offers

from services.logger import get_logger


products_bp = Blueprint(
    "products",
    __name__
)


# Logger
logger = get_logger(
    "ProductRoutes"
)


# Create platform manager
platform_manager = PlatformManager(
    create_platforms()
)


# --------------------------------------------------
# SEARCH PRODUCTS
# --------------------------------------------------

@products_bp.route("/api/products/search")
def search_products():

    query = request.args.get(
        "q",
        ""
    ).strip()

    logger.info(
        f"Product search: {query}"
    )

    if not query:

        return jsonify([])

    matches = find_matching_products(
        query
    )

    results = []

    for match in matches:

        product = match["product"]

        score = match["score"]

        # Get offers using cache service
        offers_from_db = get_product_offers(
            product,
            platform_manager
        )

        offers = []

        for offer in offers_from_db:

            offers.append({

                "platform":
                    offer.platform.name,

                "price":
                    offer.price,

                "original_price":
                    offer.original_price,

                "availability":
                    offer.availability,

                "product_url":
                    offer.product_url,

                "image_url":
                    offer.image_url,

                "last_updated":
                    (
                        offer.last_updated.isoformat()
                        if offer.last_updated
                        else None
                    )
            })

        # Keep only available offers
        available_offers = [

            offer

            for offer in offers

            if offer["availability"].lower()
            == "available"

        ]

        # Sort by lowest price
        available_offers.sort(
            key=lambda x: x["price"]
        )

        if available_offers:

            lowest_price = (
                available_offers[0]["price"]
            )

            highest_price = (
                available_offers[-1]["price"]
            )

            for offer in available_offers:

                offer["is_lowest"] = (
                    offer["price"]
                    == lowest_price
                )

                offer["saving"] = round(
                    highest_price
                    - offer["price"],
                    2
                )

                if highest_price > 0:

                    offer[
                        "saving_percentage"
                    ] = round(

                        (
                            (
                                highest_price
                                - offer["price"]
                            )
                            /
                            highest_price
                        )
                        * 100,

                        2
                    )

                else:

                    offer[
                        "saving_percentage"
                    ] = 0

            best_price = lowest_price

            best_platform = (
                available_offers[0]["platform"]
            )

            total_savings = round(
                highest_price
                - lowest_price,
                2
            )

        else:

            best_price = None

            best_platform = None

            highest_price = None

            total_savings = 0

        results.append({

            "id":
                product.id,

            "name":
                product.name,

            "brand":
                product.brand,

            "category":
                product.category,

            "description":
                product.description,

            "image_url":
                product.image_url,

            "storage":
                product.storage,

            "model_number":
                product.model_number,

            "color":
                product.color,

            "match_score":
                score,

            "best_price":
                best_price,

            "best_platform":
                best_platform,

            "highest_price":
                highest_price,

            "total_savings":
                total_savings,

            "offer_count":
                len(available_offers),

            "offers":
                available_offers

        })

    logger.info(
        f"Search completed: {query} | "
        f"Results: {len(results)}"
    )

    return jsonify(results)


# --------------------------------------------------
# PRODUCT DETAILS API
# --------------------------------------------------

@products_bp.route(
    "/api/products/<int:product_id>"
)
def product_details(product_id):

    logger.info(
        f"Product details requested: "
        f"{product_id}"
    )

    product = Product.query.get(
        product_id
    )

    if not product:

        logger.warning(
            f"Product not found: "
            f"{product_id}"
        )

        return jsonify({

            "error":
                "Product not found"

        }), 404

    # Get offers using cache service
    offers_from_db = get_product_offers(
        product,
        platform_manager
    )

    offers = []

    for offer in offers_from_db:

        offers.append({

            "platform":
                offer.platform.name,

            "price":
                offer.price,

            "original_price":
                offer.original_price,

            "availability":
                offer.availability,

            "product_url":
                offer.product_url,

            "image_url":
                offer.image_url,

            "last_updated":
                (
                    offer.last_updated.isoformat()
                    if offer.last_updated
                    else None
                )
        })

    # Keep available offers only
    available_offers = [

        offer

        for offer in offers

        if offer["availability"].lower()
        == "available"

    ]

    # Sort by price
    available_offers.sort(
        key=lambda x: x["price"]
    )

    if available_offers:

        best_price = (
            available_offers[0]["price"]
        )

        best_platform = (
            available_offers[0]["platform"]
        )

        highest_price = (
            available_offers[-1]["price"]
        )

        total_savings = round(

            highest_price
            - best_price,

            2
        )

    else:

        best_price = None

        best_platform = None

        highest_price = None

        total_savings = 0

    # Mark lowest price
    for offer in available_offers:

        offer["is_lowest"] = (

            offer["price"]
            == best_price

        )

    logger.info(
        f"Product details loaded: "
        f"{product.name}"
    )

    return jsonify({

        "id":
            product.id,

        "name":
            product.name,

        "brand":
            product.brand,

        "category":
            product.category,

        "description":
            product.description,

        "image_url":
            product.image_url,

        "storage":
            product.storage,

        "model_number":
            product.model_number,

        "color":
            product.color,

        "best_price":
            best_price,

        "best_platform":
            best_platform,

        "highest_price":
            highest_price,

        "total_savings":
            total_savings,

        "offer_count":
            len(available_offers),

        "offers":
            available_offers

    })


# --------------------------------------------------
# PRODUCT PAGE
# --------------------------------------------------

@products_bp.route(
    "/product/<int:product_id>"
)
def product_page(product_id):

    logger.info(
        f"Product page opened: "
        f"{product_id}"
    )

    return render_template(

        "product.html",

        product_id=product_id

    )