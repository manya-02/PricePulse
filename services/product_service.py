from services.offer_matcher import (
    match_platform_product
)

from models.product import Product

from services.product_matcher import (
    similarity_score,
    extract_storage,
    extract_model_number,
    extract_brand,
    extract_color,
    normalize_product_name,
    get_tokens
)


def find_matching_products(query):

    products = Product.query.all()

    matches = []

    query = query.strip()

    if not query:
        return []


    # ---------------------------------------------------------
    # QUERY INFORMATION
    # ---------------------------------------------------------

    query_storage = extract_storage(query)

    query_model = extract_model_number(query)

    query_brand = extract_brand(query)

    query_color = extract_color(query)

    query_tokens = get_tokens(query)


    # ---------------------------------------------------------
    # CATEGORY ALIASES
    # ---------------------------------------------------------

    category_aliases = {

        "mobile": {
            "mobile",
            "mobiles",
            "phone",
            "phones",
            "smartphone",
            "smartphones"
        },

        "laptop": {
            "laptop",
            "laptops",
            "notebook",
            "notebooks"
        },

        "audio": {
            "audio",
            "earbud",
            "earbuds",
            "headphone",
            "headphones",
            "airpods"
        },

        "smartwatch": {
            "smartwatch",
            "smartwatches",
            "watch",
            "watches"
        },

        "television": {
            "tv",
            "television",
            "televisions"
        },

        "gaming": {
            "gaming",
            "game",
            "games",
            "console",
            "consoles"
        },

        "monitor": {
            "monitor",
            "monitors",
            "display",
            "displays"
        },

        "camera": {
            "camera",
            "cameras"
        },

        "accessories": {
            "accessory",
            "accessories",
            "keyboard",
            "keyboards",
            "mouse",
            "mice"
        },

        "home appliance": {
            "appliance",
            "appliances",
            "vacuum",
            "purifier",
            "washing",
            "washingmachine",
            "fan"
        },

        "kitchen appliance": {
            "kitchen",
            "microwave",
            "airfryer",
            "air",
            "fryer"
        },

        "personal care": {
            "personal",
            "care",
            "trimmer",
            "hairdryer",
            "dryer"
        }

    }


    # ---------------------------------------------------------
    # FIND CATEGORY FROM QUERY
    # ---------------------------------------------------------

    query_category = None

    normalized_query = normalize_product_name(query)

    for category, aliases in category_aliases.items():

        query_words = set(
            normalized_query.split()
        )

        if query_words.intersection(aliases):

            query_category = category

            break


    # ---------------------------------------------------------
    # CHECK EACH PRODUCT
    # ---------------------------------------------------------

    for product in products:

        # -----------------------------------------------------
        # BUILD PRODUCT SEARCH TEXT
        # -----------------------------------------------------

        product_text = product.name or ""


        if product.brand:

            product_text += (
                " " + product.brand
            )


        if product.category:

            product_text += (
                " " + product.category
            )


        if product.storage:

            product_text += (
                " " + product.storage
            )


        if product.color:

            product_text += (
                " " + product.color
            )


        if product.model_number:

            product_text += (
                " " + product.model_number
            )


        # -----------------------------------------------------
        # NORMALIZED PRODUCT TOKENS
        # -----------------------------------------------------

        product_tokens = get_tokens(
            product_text
        )


        matching_tokens = (
            query_tokens.intersection(
                product_tokens
            )
        )


        all_query_tokens_present = all(

            token in product_tokens

            for token in query_tokens

        )


        # -----------------------------------------------------
        # CATEGORY MATCH
        # -----------------------------------------------------

        category_match = False


        if query_category:

            database_category = (
                (product.category or "")
                .lower()
                .strip()
            )


            # Direct category match

            if database_category == query_category:

                category_match = True


            # Home appliance aliases

            elif (
                query_category == "home appliance"
                and database_category == "home appliance"
            ):

                category_match = True


            # Kitchen appliance

            elif (
                query_category == "kitchen appliance"
                and database_category == "kitchen appliance"
            ):

                category_match = True


            # Personal care

            elif (
                query_category == "personal care"
                and database_category == "personal care"
            ):

                category_match = True


        # -----------------------------------------------------
        # SIMILARITY SCORE
        # -----------------------------------------------------

        score = similarity_score(

            query,

            product_text

        )


        # -----------------------------------------------------
        # STORAGE FILTER
        # -----------------------------------------------------

        if query_storage:

            if not product.storage:

                continue


            if (
                product.storage.lower()
                != query_storage.lower()
            ):

                continue


        # -----------------------------------------------------
        # MODEL FILTER
        # -----------------------------------------------------

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


        # -----------------------------------------------------
        # BRAND FILTER
        # -----------------------------------------------------

        if query_brand:

            if not product.brand:

                continue


            database_brand = (
                product.brand.lower()
            )


            if database_brand != query_brand:

                continue


        # -----------------------------------------------------
        # COLOR FILTER
        # -----------------------------------------------------

        if query_color:

            if not product.color:

                continue


            database_color = (
                product.color.lower()
            )


            if database_color != query_color:

                continue


        # -----------------------------------------------------
        # CATEGORY SEARCH
        # -----------------------------------------------------

        if category_match:

            search_score = max(

                score,

                75

            )


        # -----------------------------------------------------
        # EXACT TOKEN MATCH
        # -----------------------------------------------------

        elif all_query_tokens_present:

            search_score = max(

                score,

                70

            )


        # -----------------------------------------------------
        # PARTIAL TOKEN MATCH
        # -----------------------------------------------------

        elif matching_tokens:

            token_ratio = (

                len(matching_tokens)

                /

                len(query_tokens)

            )


            search_score = max(

                score,

                token_ratio * 60

            )


        else:

            search_score = score


        # -----------------------------------------------------
        # MINIMUM SCORE
        # -----------------------------------------------------

        if search_score < 30:

            continue


        # -----------------------------------------------------
        # ADD RESULT
        # -----------------------------------------------------

        matches.append({

            "product": product,

            "score": round(

                search_score,

                2

            )

        })


    # ---------------------------------------------------------
    # SORT RESULTS
    # ---------------------------------------------------------

    matches.sort(

        key=lambda x: x["score"],

        reverse=True

    )


    return matches



# =============================================================
# PLATFORM PRODUCT MATCHING
# =============================================================

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

                "product": product,

                "score": result["score"]

            })


    matches.sort(

        key=lambda x: x["score"],

        reverse=True

    )


    return matches