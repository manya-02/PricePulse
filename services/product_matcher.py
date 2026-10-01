import re

from difflib import SequenceMatcher


# ----------------------------------
# NORMALIZATION
# ----------------------------------

def normalize_product_name(name):

    if not name:

        return ""

    name = name.lower().strip()

    # Convert "128 GB" → "128gb"
    name = re.sub(
        r"(\d+)\s*gb",
        r"\1gb",
        name
    )

    # Convert "1 TB" → "1tb"
    name = re.sub(
        r"(\d+)\s*tb",
        r"\1tb",
        name
    )

    # Replace separators
    name = re.sub(
        r"[-_/]",
        " ",
        name
    )

    # Remove brackets
    name = re.sub(
        r"[\(\)\[\]\{\}]",
        " ",
        name
    )

    # Remove special characters
    name = re.sub(
        r"[^a-z0-9\s]",
        " ",
        name
    )

    # Separate letters and numbers
    name = re.sub(
        r"([a-z])(\d)",
        r"\1 \2",
        name
    )

    name = re.sub(
        r"(\d)([a-z])",
        r"\1 \2",
        name
    )

    # Convert "128 gb" → "128gb"
    name = re.sub(
        r"(\d+)\s+(gb|tb)",
        r"\1\2",
        name
    )

    # Remove extra spaces
    name = re.sub(
        r"\s+",
        " ",
        name
    ).strip()

    return name


# ----------------------------------
# TOKENS
# ----------------------------------

def get_tokens(name):

    normalized = normalize_product_name(
        name
    )

    return set(
        normalized.split()
    )


# ----------------------------------
# STORAGE
# ----------------------------------

def extract_storage(name):

    normalized = normalize_product_name(
        name
    )

    match = re.search(
        r"\b(\d+)(gb|tb)\b",
        normalized
    )

    if match:

        return match.group(0)

    return None


# ----------------------------------
# MODEL NUMBER
# ----------------------------------

def extract_model_number(name):

    normalized = normalize_product_name(
        name
    )

    patterns = [

        r"\biphone\s+\d+\b",

        r"\bgalaxy\s+s\d+\b",

        r"\bpixel\s+\d+\b",

        r"\bredmi\s+\w*\s*\d+\b",

        r"\bpoco\s+\w*\s*\d+\b",

        r"\boneplus\s+\d+\b",

        r"\brealme\s+\w*\s*\d+\b",

        r"\boppo\s+\w*\s*\d+\b",

        r"\bvivo\s+\w*\s*\d+\b"

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            normalized
        )

        if match:

            return match.group(0)

    return None


# ----------------------------------
# BRAND
# ----------------------------------

def extract_brand(name):

    normalized = normalize_product_name(
        name
    )

    brands = [

        "apple",

        "samsung",

        "google",

        "xiaomi",

        "redmi",

        "poco",

        "oneplus",

        "realme",

        "oppo",

        "vivo"

    ]

    words = normalized.split()

    for brand in brands:

        if brand in words:

            return brand

    return None


# ----------------------------------
# COLOR
# ----------------------------------

def extract_color(name):

    normalized = normalize_product_name(
        name
    )

    colors = [

        "black",

        "white",

        "blue",

        "red",

        "green",

        "yellow",

        "pink",

        "purple",

        "gold",

        "silver",

        "grey",

        "gray",

        "orange",

        "brown"

    ]

    words = normalized.split()

    for color in colors:

        if color in words:

            return color

    return None


# ----------------------------------
# TOKEN SIMILARITY
# ----------------------------------

def token_similarity(
    name1,
    name2
):

    tokens1 = get_tokens(name1)

    tokens2 = get_tokens(name2)

    if not tokens1 or not tokens2:

        return 0

    common_tokens = (
        tokens1.intersection(tokens2)
    )

    total_tokens = (
        tokens1.union(tokens2)
    )

    return (
        len(common_tokens)
        /
        len(total_tokens)
    ) * 100


# ----------------------------------
# TEXT SIMILARITY
# ----------------------------------

def text_similarity(
    name1,
    name2
):

    normalized1 = (
        normalize_product_name(name1)
    )

    normalized2 = (
        normalize_product_name(name2)
    )

    return (

        SequenceMatcher(

            None,

            normalized1,

            normalized2

        ).ratio()

        * 100

    )


# ----------------------------------
# SIMILARITY SCORE
# ----------------------------------

def similarity_score(
    name1,
    name2
):

    text_score = text_similarity(
        name1,
        name2
    )

    token_score = token_similarity(
        name1,
        name2
    )

    # Base score
    score = (

        text_score * 0.5

        +

        token_score * 0.5

    )

    # ----------------------------------
    # Storage comparison
    # ----------------------------------

    storage1 = extract_storage(name1)

    storage2 = extract_storage(name2)

    if storage1 and storage2:

        if storage1 != storage2:

            return round(
                score * 0.35,
                2
            )

        score += 10

    # ----------------------------------
    # Model comparison
    # ----------------------------------

    model1 = extract_model_number(name1)

    model2 = extract_model_number(name2)

    if model1 and model2:

        if model1 != model2:

            return round(
                score * 0.35,
                2
            )

        score += 10

    # ----------------------------------
    # Brand comparison
    # ----------------------------------

    brand1 = extract_brand(name1)

    brand2 = extract_brand(name2)

    if brand1 and brand2:

        if brand1 != brand2:

            return round(
                score * 0.35,
                2
            )

        score += 5

    # ----------------------------------
    # Color comparison
    # ----------------------------------

    color1 = extract_color(name1)

    color2 = extract_color(name2)

    if color1 and color2:

        if color1 != color2:

            return round(
                score * 0.80,
                2
            )

        score += 2

    return round(
        min(score, 100),
        2
    )