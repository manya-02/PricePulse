from services.product_matcher import (
    similarity_score,
    extract_storage,
    extract_model_number,
    extract_brand,
    extract_color
)


def build_product_text(product):

    text = product.name

    if product.brand:

        text += " " + product.brand

    if product.storage:

        text += " " + product.storage

    if product.model_number:

        text += " " + product.model_number

    if product.color:

        text += " " + product.color

    return text


def is_same_variant(
    product,
    platform_product_name
):

    # ----------------------------------
    # Storage
    # ----------------------------------

    platform_storage = extract_storage(
        platform_product_name
    )

    if platform_storage:

        if not product.storage:

            return False

        if (
            platform_storage.lower()
            != product.storage.lower()
        ):

            return False

    # ----------------------------------
    # Model
    # ----------------------------------

    platform_model = extract_model_number(
        platform_product_name
    )

    if platform_model:

        if not product.model_number:

            return False

        database_model = extract_model_number(
            product.model_number
        )

        if database_model != platform_model:

            return False

    # ----------------------------------
    # Brand
    # ----------------------------------

    platform_brand = extract_brand(
        platform_product_name
    )

    if platform_brand:

        if not product.brand:

            return False

        if (
            product.brand.lower()
            != platform_brand
        ):

            return False

    # ----------------------------------
    # Color
    # ----------------------------------

    platform_color = extract_color(
        platform_product_name
    )

    if platform_color:

        if not product.color:

            return False

        if (
            product.color.lower()
            != platform_color
        ):

            return False

    return True


def match_platform_product(
    product,
    platform_product_name,
    minimum_score=40
):

    if not is_same_variant(
        product,
        platform_product_name
    ):

        return {

            "matched": False,

            "score": 0

        }

    database_text = build_product_text(
        product
    )

    score = similarity_score(

        database_text,

        platform_product_name

    )

    return {

        "matched":
            score >= minimum_score,

        "score":
            score

    }