from services.offer_matcher import (
    match_platform_product
)

from models.product import Product

from services.product_matcher import (
    similarity_score,
    extract_storage,
    extract_model_number,
    extract_brand,
    extract_color
)


def find_matching_products(query):

    products = Product.query.all()

    matches = []

    query_storage = extract_storage(
        query
    )

    query_model = extract_model_number(
        query
    )

    query_brand = extract_brand(
        query
    )

    query_color = extract_color(
        query
    )

    for product in products:

        product_text = product.name

        if product.brand:

            product_text += (
                " " + product.brand
            )

        if product.storage:

            product_text += (
                " " + product.storage
            )

        if product.color:

            product_text += (
                " " + product.color
            )

        score = similarity_score(
            query,
            product_text
        )

        # ----------------------------------
        # Storage filter
        # ----------------------------------

        if query_storage:

            if not product.storage:

                continue

            if (
                product.storage.lower()
                != query_storage.lower()
            ):

                continue

        # ----------------------------------
        # Model filter
        # ----------------------------------

        if query_model:

            if not product.model_number:

                continue

            database_model = (
                extract_model_number(
                    product.model_number
                )
            )

            if database_model != query_model:

                continue

        # ----------------------------------
        # Brand filter
        # ----------------------------------

        if query_brand:

            if not product.brand:

                continue

            database_brand = (
                product.brand.lower()
            )

            if database_brand != query_brand:

                continue

        # ----------------------------------
        # Color filter
        # ----------------------------------

        if query_color:

            if not product.color:

                continue

            database_color = (
                product.color.lower()
            )

            if database_color != query_color:

                continue

        # ----------------------------------
        # Minimum similarity
        # ----------------------------------

        if score < 30:

            continue

        matches.append({

            "product":
                product,

            "score":
                score

        })

    # Highest score first
    matches.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return matches

def find_platform_product_match(
    platform_product_name
):

    products = Product.query.all()

    matches = []

    for product in products:

        result = match_platform_product(

            product,

            platform_product_name

        )

        if result["matched"]:

            matches.append({

                "product":
                    product,

                "score":
                    result["score"]

            })

    matches.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return matches