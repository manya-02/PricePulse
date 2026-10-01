from services.offer_matcher import (
    is_same_variant
)


class TestProduct:

    name = "iPhone 15"

    brand = "Apple"

    storage = "128GB"

    model_number = "iPhone 15"

    color = "Black"


product = TestProduct()


tests = [

    "Apple iPhone 15 128GB Black",

    "iPhone 15 128 GB Black",

    "Apple iPhone 15 256GB Black",

    "Samsung Galaxy S24 128GB Black"

]


for name in tests:

    result = is_same_variant(
        product,
        name
    )

    print(
        name,
        "→",
        result
    )