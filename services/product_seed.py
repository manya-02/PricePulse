from models import db
from models.product import Product


def seed_products():

    products = [

        {
            "name": "iPhone 15",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 15 with 128GB storage",
            "storage": "128GB",
            "model_number": "iPhone 15",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+15"
        },

        {
            "name": "iPhone 15",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 15 with 256GB storage",
            "storage": "256GB",
            "model_number": "iPhone 15",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+15"
        },

        {
            "name": "Samsung Galaxy S24",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy S24 with 128GB storage",
            "storage": "128GB",
            "model_number": "Galaxy S24",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+S24"
        },

        {
            "name": "Samsung Galaxy S24",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy S24 with 256GB storage",
            "storage": "256GB",
            "model_number": "Galaxy S24",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+S24"
        },

        {
            "name": "Google Pixel 9",
            "brand": "Google",
            "category": "Mobile",
            "description": "Google Pixel 9 with 128GB storage",
            "storage": "128GB",
            "model_number": "Pixel 9",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Pixel+9"
        },

        {
            "name": "OnePlus 13",
            "brand": "OnePlus",
            "category": "Mobile",
            "description": "OnePlus 13 with 256GB storage",
            "storage": "256GB",
            "model_number": "OnePlus 13",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+13"
        }
    ]


    for data in products:

        existing_product = Product.query.filter_by(
            name=data["name"],
            storage=data["storage"],
            color=data["color"]
        ).first()


        if existing_product:

            # Update image if product already exists

            existing_product.image_url = data["image_url"]

            continue


        product = Product(

            name=data["name"],

            brand=data["brand"],

            category=data["category"],

            description=data["description"],

            storage=data["storage"],

            model_number=data["model_number"],

            color=data["color"],

            image_url=data["image_url"]
        )


        db.session.add(product)


    db.session.commit()