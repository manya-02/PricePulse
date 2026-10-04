from models import db
from models.product import Product


def seed_products():

    products = [

        # =========================================================
        # SMARTPHONES - APPLE
        # =========================================================

        {
            "name": "iPhone 13",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 13 with 128GB storage",
            "storage": "128GB",
            "model_number": "iPhone 13",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+13"
        },

        {
            "name": "iPhone 14",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 14 with 128GB storage",
            "storage": "128GB",
            "model_number": "iPhone 14",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+14"
        },

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
            "name": "iPhone 16",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 16 with 128GB storage",
            "storage": "128GB",
            "model_number": "iPhone 16",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+16"
        },

        {
            "name": "iPhone 16",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 16 with 256GB storage",
            "storage": "256GB",
            "model_number": "iPhone 16",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+16"
        },

        {
            "name": "iPhone 16e",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 16e with 128GB storage",
            "storage": "128GB",
            "model_number": "iPhone 16e",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+16e"
        },

        {
            "name": "iPhone 17",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 17 with 256GB storage",
            "storage": "256GB",
            "model_number": "iPhone 17",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+17"
        },

        {
            "name": "iPhone 17 Pro",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 17 Pro with 256GB storage",
            "storage": "256GB",
            "model_number": "iPhone 17 Pro",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+17+Pro"
        },

        {
            "name": "iPhone 17 Pro Max",
            "brand": "Apple",
            "category": "Mobile",
            "description": "Apple iPhone 17 Pro Max with 256GB storage",
            "storage": "256GB",
            "model_number": "iPhone 17 Pro Max",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=iPhone+17+Pro+Max"
        },


        # =========================================================
        # SMARTPHONES - SAMSUNG
        # =========================================================

        {
            "name": "Samsung Galaxy S23",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy S23 with 128GB storage",
            "storage": "128GB",
            "model_number": "Galaxy S23",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+S23"
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
            "name": "Samsung Galaxy S24 FE",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy S24 FE with 128GB storage",
            "storage": "128GB",
            "model_number": "Galaxy S24 FE",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+S24+FE"
        },

        {
            "name": "Samsung Galaxy S25",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy S25 with 128GB storage",
            "storage": "128GB",
            "model_number": "Galaxy S25",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+S25"
        },

        {
            "name": "Samsung Galaxy S25",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy S25 with 256GB storage",
            "storage": "256GB",
            "model_number": "Galaxy S25",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+S25"
        },

        {
            "name": "Samsung Galaxy A35",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy A35 with 128GB storage",
            "storage": "128GB",
            "model_number": "Galaxy A35",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+A35"
        },

        {
            "name": "Samsung Galaxy A55",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy A55 with 128GB storage",
            "storage": "128GB",
            "model_number": "Galaxy A55",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+A55"
        },

        {
            "name": "Samsung Galaxy A55",
            "brand": "Samsung",
            "category": "Mobile",
            "description": "Samsung Galaxy A55 with 256GB storage",
            "storage": "256GB",
            "model_number": "Galaxy A55",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+A55"
        },


        # =========================================================
        # SMARTPHONES - GOOGLE
        # =========================================================

        {
            "name": "Google Pixel 8",
            "brand": "Google",
            "category": "Mobile",
            "description": "Google Pixel 8 with 128GB storage",
            "storage": "128GB",
            "model_number": "Pixel 8",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Pixel+8"
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
            "name": "Google Pixel 9 Pro",
            "brand": "Google",
            "category": "Mobile",
            "description": "Google Pixel 9 Pro with 128GB storage",
            "storage": "128GB",
            "model_number": "Pixel 9 Pro",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Pixel+9+Pro"
        },

        {
            "name": "Google Pixel 9 Pro",
            "brand": "Google",
            "category": "Mobile",
            "description": "Google Pixel 9 Pro with 256GB storage",
            "storage": "256GB",
            "model_number": "Pixel 9 Pro",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Pixel+9+Pro"
        },

        {
            "name": "Google Pixel 9a",
            "brand": "Google",
            "category": "Mobile",
            "description": "Google Pixel 9a with 128GB storage",
            "storage": "128GB",
            "model_number": "Pixel 9a",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Pixel+9a"
        },

        {
            "name": "Google Pixel 10",
            "brand": "Google",
            "category": "Mobile",
            "description": "Google Pixel 10 with 128GB storage",
            "storage": "128GB",
            "model_number": "Pixel 10",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Pixel+10"
        },


        # =========================================================
        # SMARTPHONES - ONEPLUS
        # =========================================================

        {
            "name": "OnePlus 12",
            "brand": "OnePlus",
            "category": "Mobile",
            "description": "OnePlus 12 with 256GB storage",
            "storage": "256GB",
            "model_number": "OnePlus 12",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+12"
        },

        {
            "name": "OnePlus 12R",
            "brand": "OnePlus",
            "category": "Mobile",
            "description": "OnePlus 12R with 128GB storage",
            "storage": "128GB",
            "model_number": "OnePlus 12R",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+12R"
        },

        {
            "name": "OnePlus 12R",
            "brand": "OnePlus",
            "category": "Mobile",
            "description": "OnePlus 12R with 256GB storage",
            "storage": "256GB",
            "model_number": "OnePlus 12R",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+12R"
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
        },

        {
            "name": "OnePlus 13R",
            "brand": "OnePlus",
            "category": "Mobile",
            "description": "OnePlus 13R with 256GB storage",
            "storage": "256GB",
            "model_number": "OnePlus 13R",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+13R"
        },

        {
            "name": "OnePlus Nord 4",
            "brand": "OnePlus",
            "category": "Mobile",
            "description": "OnePlus Nord 4 with 128GB storage",
            "storage": "128GB",
            "model_number": "OnePlus Nord 4",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Nord+4"
        },

        {
            "name": "OnePlus Nord CE4",
            "brand": "OnePlus",
            "category": "Mobile",
            "description": "OnePlus Nord CE4 with 128GB storage",
            "storage": "128GB",
            "model_number": "OnePlus Nord CE4",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Nord+CE4"
        },


        # =========================================================
        # SMARTPHONES - OTHER BRANDS
        # =========================================================

        {
            "name": "Nothing Phone 2",
            "brand": "Nothing",
            "category": "Mobile",
            "description": "Nothing Phone 2 with 128GB storage",
            "storage": "128GB",
            "model_number": "Nothing Phone 2",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Nothing+Phone+2"
        },

        {
            "name": "Nothing Phone 3",
            "brand": "Nothing",
            "category": "Mobile",
            "description": "Nothing Phone 3 with 256GB storage",
            "storage": "256GB",
            "model_number": "Nothing Phone 3",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Nothing+Phone+3"
        },

        {
            "name": "Xiaomi 14",
            "brand": "Xiaomi",
            "category": "Mobile",
            "description": "Xiaomi 14 with 512GB storage",
            "storage": "512GB",
            "model_number": "Xiaomi 14",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Xiaomi+14"
        },

        {
            "name": "Xiaomi 15",
            "brand": "Xiaomi",
            "category": "Mobile",
            "description": "Xiaomi 15 with 256GB storage",
            "storage": "256GB",
            "model_number": "Xiaomi 15",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Xiaomi+15"
        },

        {
            "name": "Redmi Note 14 Pro",
            "brand": "Redmi",
            "category": "Mobile",
            "description": "Redmi Note 14 Pro with 128GB storage",
            "storage": "128GB",
            "model_number": "Redmi Note 14 Pro",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Redmi+Note+14+Pro"
        },

        {
            "name": "Motorola Edge 50 Pro",
            "brand": "Motorola",
            "category": "Mobile",
            "description": "Motorola Edge 50 Pro with 256GB storage",
            "storage": "256GB",
            "model_number": "Edge 50 Pro",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Edge+50+Pro"
        },

        {
            "name": "Motorola Edge 60 Pro",
            "brand": "Motorola",
            "category": "Mobile",
            "description": "Motorola Edge 60 Pro with 256GB storage",
            "storage": "256GB",
            "model_number": "Edge 60 Pro",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Edge+60+Pro"
        },

        {
            "name": "Realme GT 6",
            "brand": "Realme",
            "category": "Mobile",
            "description": "Realme GT 6 with 256GB storage",
            "storage": "256GB",
            "model_number": "GT 6",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Realme+GT+6"
        },

        {
            "name": "Vivo V40",
            "brand": "Vivo",
            "category": "Mobile",
            "description": "Vivo V40 with 128GB storage",
            "storage": "128GB",
            "model_number": "V40",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Vivo+V40"
        },

        {
            "name": "Oppo Reno 12",
            "brand": "Oppo",
            "category": "Mobile",
            "description": "Oppo Reno 12 with 256GB storage",
            "storage": "256GB",
            "model_number": "Reno 12",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Oppo+Reno+12"
        },


        # =========================================================
        # LAPTOPS
        # =========================================================

        {
            "name": "MacBook Air M2",
            "brand": "Apple",
            "category": "Laptop",
            "description": "Apple MacBook Air with M2 chip and 256GB SSD",
            "storage": "256GB",
            "model_number": "MacBook Air M2",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=MacBook+Air+M2"
        },

        {
            "name": "MacBook Air M3",
            "brand": "Apple",
            "category": "Laptop",
            "description": "Apple MacBook Air with M3 chip and 256GB SSD",
            "storage": "256GB",
            "model_number": "MacBook Air M3",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=MacBook+Air+M3"
        },

        {
            "name": "MacBook Air M4",
            "brand": "Apple",
            "category": "Laptop",
            "description": "Apple MacBook Air with M4 chip and 256GB SSD",
            "storage": "256GB",
            "model_number": "MacBook Air M4",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=MacBook+Air+M4"
        },

        {
            "name": "MacBook Pro M4",
            "brand": "Apple",
            "category": "Laptop",
            "description": "Apple MacBook Pro with M4 chip and 512GB SSD",
            "storage": "512GB",
            "model_number": "MacBook Pro M4",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=MacBook+Pro+M4"
        },

        {
            "name": "Dell Inspiron 15",
            "brand": "Dell",
            "category": "Laptop",
            "description": "Dell Inspiron 15 laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "Inspiron 15",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=Dell+Inspiron+15"
        },

        {
            "name": "Dell XPS 13",
            "brand": "Dell",
            "category": "Laptop",
            "description": "Dell XPS 13 laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "XPS 13",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=Dell+XPS+13"
        },

        {
            "name": "HP Pavilion 14",
            "brand": "HP",
            "category": "Laptop",
            "description": "HP Pavilion 14 laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "Pavilion 14",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=HP+Pavilion+14"
        },

        {
            "name": "HP Victus 15",
            "brand": "HP",
            "category": "Laptop",
            "description": "HP Victus 15 gaming laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "Victus 15",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=HP+Victus+15"
        },

        {
            "name": "Lenovo IdeaPad Slim 5",
            "brand": "Lenovo",
            "category": "Laptop",
            "description": "Lenovo IdeaPad Slim 5 with 512GB SSD",
            "storage": "512GB",
            "model_number": "IdeaPad Slim 5",
            "color": "Grey",
            "image_url": "https://placehold.co/400x400?text=IdeaPad+Slim+5"
        },

        {
            "name": "Lenovo LOQ",
            "brand": "Lenovo",
            "category": "Laptop",
            "description": "Lenovo LOQ gaming laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "LOQ",
            "color": "Grey",
            "image_url": "https://placehold.co/400x400?text=Lenovo+LOQ"
        },

        {
            "name": "Lenovo Legion 5",
            "brand": "Lenovo",
            "category": "Laptop",
            "description": "Lenovo Legion 5 gaming laptop with 1TB SSD",
            "storage": "1TB",
            "model_number": "Legion 5",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Legion+5"
        },

        {
            "name": "ASUS Vivobook 15",
            "brand": "ASUS",
            "category": "Laptop",
            "description": "ASUS Vivobook 15 laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "Vivobook 15",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=ASUS+Vivobook+15"
        },

        {
            "name": "ASUS TUF Gaming F15",
            "brand": "ASUS",
            "category": "Laptop",
            "description": "ASUS TUF Gaming F15 laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "TUF Gaming F15",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=ASUS+TUF+F15"
        },

        {
            "name": "Acer Aspire 5",
            "brand": "Acer",
            "category": "Laptop",
            "description": "Acer Aspire 5 laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "Aspire 5",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=Acer+Aspire+5"
        },

        {
            "name": "Acer Nitro V",
            "brand": "Acer",
            "category": "Laptop",
            "description": "Acer Nitro V gaming laptop with 512GB SSD",
            "storage": "512GB",
            "model_number": "Nitro V",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Acer+Nitro+V"
        },


        # =========================================================
        # EARBUDS / HEADPHONES
        # =========================================================

        {
            "name": "AirPods 2",
            "brand": "Apple",
            "category": "Audio",
            "description": "Apple AirPods 2 wireless earbuds",
            "storage": "",
            "model_number": "AirPods 2",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=AirPods+2"
        },

        {
            "name": "AirPods 3",
            "brand": "Apple",
            "category": "Audio",
            "description": "Apple AirPods 3 wireless earbuds",
            "storage": "",
            "model_number": "AirPods 3",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=AirPods+3"
        },

        {
            "name": "AirPods 4",
            "brand": "Apple",
            "category": "Audio",
            "description": "Apple AirPods 4 wireless earbuds",
            "storage": "",
            "model_number": "AirPods 4",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=AirPods+4"
        },

        {
            "name": "AirPods Pro 2",
            "brand": "Apple",
            "category": "Audio",
            "description": "Apple AirPods Pro 2 wireless earbuds",
            "storage": "",
            "model_number": "AirPods Pro 2",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=AirPods+Pro+2"
        },

        {
            "name": "Samsung Galaxy Buds FE",
            "brand": "Samsung",
            "category": "Audio",
            "description": "Samsung Galaxy Buds FE wireless earbuds",
            "storage": "",
            "model_number": "Galaxy Buds FE",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+Buds+FE"
        },

        {
            "name": "Galaxy Buds 3",
            "brand": "Samsung",
            "category": "Audio",
            "description": "Samsung Galaxy Buds 3 wireless earbuds",
            "storage": "",
            "model_number": "Galaxy Buds 3",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=Galaxy+Buds+3"
        },

        {
            "name": "OnePlus Buds 3",
            "brand": "OnePlus",
            "category": "Audio",
            "description": "OnePlus Buds 3 wireless earbuds",
            "storage": "",
            "model_number": "Buds 3",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+Buds+3"
        },

        {
            "name": "OnePlus Buds Pro 3",
            "brand": "OnePlus",
            "category": "Audio",
            "description": "OnePlus Buds Pro 3 wireless earbuds",
            "storage": "",
            "model_number": "Buds Pro 3",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+Buds+Pro+3"
        },

        {
            "name": "Nothing Ear",
            "brand": "Nothing",
            "category": "Audio",
            "description": "Nothing Ear wireless earbuds",
            "storage": "",
            "model_number": "Nothing Ear",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=Nothing+Ear"
        },

        {
            "name": "Sony WH-1000XM5",
            "brand": "Sony",
            "category": "Audio",
            "description": "Sony WH-1000XM5 wireless noise cancelling headphones",
            "storage": "",
            "model_number": "WH-1000XM5",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Sony+WH-1000XM5"
        },

        {
            "name": "Sony WH-1000XM6",
            "brand": "Sony",
            "category": "Audio",
            "description": "Sony WH-1000XM6 wireless noise cancelling headphones",
            "storage": "",
            "model_number": "WH-1000XM6",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Sony+WH-1000XM6"
        },

        {
            "name": "JBL Tune 770NC",
            "brand": "JBL",
            "category": "Audio",
            "description": "JBL Tune 770NC wireless headphones",
            "storage": "",
            "model_number": "Tune 770NC",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=JBL+Tune+770NC"
        },


        # =========================================================
        # SMARTWATCHES
        # =========================================================

        {
            "name": "Apple Watch SE",
            "brand": "Apple",
            "category": "Smartwatch",
            "description": "Apple Watch SE smartwatch",
            "storage": "",
            "model_number": "Watch SE",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Apple+Watch+SE"
        },

        {
            "name": "Apple Watch Series 10",
            "brand": "Apple",
            "category": "Smartwatch",
            "description": "Apple Watch Series 10 smartwatch",
            "storage": "",
            "model_number": "Watch Series 10",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Apple+Watch+10"
        },

        {
            "name": "Apple Watch Series 11",
            "brand": "Apple",
            "category": "Smartwatch",
            "description": "Apple Watch Series 11 smartwatch",
            "storage": "",
            "model_number": "Watch Series 11",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Apple+Watch+11"
        },

        {
            "name": "Samsung Galaxy Watch 7",
            "brand": "Samsung",
            "category": "Smartwatch",
            "description": "Samsung Galaxy Watch 7 smartwatch",
            "storage": "",
            "model_number": "Galaxy Watch 7",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+Watch+7"
        },

        {
            "name": "Samsung Galaxy Watch 8",
            "brand": "Samsung",
            "category": "Smartwatch",
            "description": "Samsung Galaxy Watch 8 smartwatch",
            "storage": "",
            "model_number": "Galaxy Watch 8",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Galaxy+Watch+8"
        },

        {
            "name": "OnePlus Watch 2",
            "brand": "OnePlus",
            "category": "Smartwatch",
            "description": "OnePlus Watch 2 smartwatch",
            "storage": "",
            "model_number": "Watch 2",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+Watch+2"
        },

        {
            "name": "Google Pixel Watch 3",
            "brand": "Google",
            "category": "Smartwatch",
            "description": "Google Pixel Watch 3 smartwatch",
            "storage": "",
            "model_number": "Pixel Watch 3",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Pixel+Watch+3"
        },


        # =========================================================
        # TELEVISIONS
        # =========================================================

        {
            "name": "Samsung 43 Inch 4K Smart TV",
            "brand": "Samsung",
            "category": "Television",
            "description": "Samsung 43 inch 4K Smart TV",
            "storage": "",
            "model_number": "Samsung 43 4K TV",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Samsung+43+TV"
        },

        {
            "name": "Samsung 55 Inch 4K Smart TV",
            "brand": "Samsung",
            "category": "Television",
            "description": "Samsung 55 inch 4K Smart TV",
            "storage": "",
            "model_number": "Samsung 55 4K TV",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Samsung+55+TV"
        },

        {
            "name": "LG 43 Inch 4K Smart TV",
            "brand": "LG",
            "category": "Television",
            "description": "LG 43 inch 4K Smart TV",
            "storage": "",
            "model_number": "LG 43 4K TV",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=LG+43+TV"
        },

        {
            "name": "LG 55 Inch 4K Smart TV",
            "brand": "LG",
            "category": "Television",
            "description": "LG 55 inch 4K Smart TV",
            "storage": "",
            "model_number": "LG 55 4K TV",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=LG+55+TV"
        },

        {
            "name": "Sony Bravia 43 Inch 4K TV",
            "brand": "Sony",
            "category": "Television",
            "description": "Sony Bravia 43 inch 4K Smart TV",
            "storage": "",
            "model_number": "Bravia 43 4K",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Sony+Bravia+43"
        },

        {
            "name": "Sony Bravia 55 Inch 4K TV",
            "brand": "Sony",
            "category": "Television",
            "description": "Sony Bravia 55 inch 4K Smart TV",
            "storage": "",
            "model_number": "Bravia 55 4K",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Sony+Bravia+55"
        },

        {
            "name": "Xiaomi 43 Inch Smart TV",
            "brand": "Xiaomi",
            "category": "Television",
            "description": "Xiaomi 43 inch Smart TV",
            "storage": "",
            "model_number": "Xiaomi 43 TV",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Xiaomi+43+TV"
        },

        {
            "name": "OnePlus 43 Inch Smart TV",
            "brand": "OnePlus",
            "category": "Television",
            "description": "OnePlus 43 inch Smart TV",
            "storage": "",
            "model_number": "OnePlus 43 TV",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=OnePlus+43+TV"
        },


        # =========================================================
        # GAMING
        # =========================================================

        {
            "name": "PlayStation 5",
            "brand": "Sony",
            "category": "Gaming",
            "description": "Sony PlayStation 5 gaming console",
            "storage": "825GB",
            "model_number": "PlayStation 5",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=PlayStation+5"
        },

        {
            "name": "PlayStation 5 Slim",
            "brand": "Sony",
            "category": "Gaming",
            "description": "Sony PlayStation 5 Slim gaming console",
            "storage": "1TB",
            "model_number": "PlayStation 5 Slim",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=PS5+Slim"
        },

        {
            "name": "Xbox Series X",
            "brand": "Microsoft",
            "category": "Gaming",
            "description": "Microsoft Xbox Series X gaming console",
            "storage": "1TB",
            "model_number": "Xbox Series X",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Xbox+Series+X"
        },

        {
            "name": "Xbox Series S",
            "brand": "Microsoft",
            "category": "Gaming",
            "description": "Microsoft Xbox Series S gaming console",
            "storage": "512GB",
            "model_number": "Xbox Series S",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=Xbox+Series+S"
        },

        {
            "name": "Nintendo Switch OLED",
            "brand": "Nintendo",
            "category": "Gaming",
            "description": "Nintendo Switch OLED gaming console",
            "storage": "64GB",
            "model_number": "Switch OLED",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=Switch+OLED"
        },

        {
            "name": "Xbox Wireless Controller",
            "brand": "Microsoft",
            "category": "Gaming",
            "description": "Xbox Wireless Controller",
            "storage": "",
            "model_number": "Xbox Wireless Controller",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Xbox+Controller"
        },

        {
            "name": "DualSense Wireless Controller",
            "brand": "Sony",
            "category": "Gaming",
            "description": "Sony DualSense Wireless Controller",
            "storage": "",
            "model_number": "DualSense",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=DualSense"
        },


        # =========================================================
        # MONITORS
        # =========================================================

        {
            "name": "LG 24 Inch Full HD Monitor",
            "brand": "LG",
            "category": "Monitor",
            "description": "LG 24 inch Full HD monitor",
            "storage": "",
            "model_number": "LG 24 FHD",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=LG+24+Monitor"
        },

        {
            "name": "Samsung 24 Inch Full HD Monitor",
            "brand": "Samsung",
            "category": "Monitor",
            "description": "Samsung 24 inch Full HD monitor",
            "storage": "",
            "model_number": "Samsung 24 FHD",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Samsung+24+Monitor"
        },

        {
            "name": "Dell 24 Inch Monitor",
            "brand": "Dell",
            "category": "Monitor",
            "description": "Dell 24 inch Full HD monitor",
            "storage": "",
            "model_number": "Dell 24 Monitor",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Dell+24+Monitor"
        },

        {
            "name": "LG 27 Inch QHD Monitor",
            "brand": "LG",
            "category": "Monitor",
            "description": "LG 27 inch QHD monitor",
            "storage": "",
            "model_number": "LG 27 QHD",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=LG+27+Monitor"
        },

        {
            "name": "Samsung 27 Inch Gaming Monitor",
            "brand": "Samsung",
            "category": "Monitor",
            "description": "Samsung 27 inch gaming monitor",
            "storage": "",
            "model_number": "Samsung 27 Gaming",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Samsung+27+Gaming"
        },


        # =========================================================
        # KEYBOARDS AND MICE
        # =========================================================

        {
            "name": "Logitech G102",
            "brand": "Logitech",
            "category": "Accessories",
            "description": "Logitech G102 gaming mouse",
            "storage": "",
            "model_number": "G102",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Logitech+G102"
        },

        {
            "name": "Logitech G502",
            "brand": "Logitech",
            "category": "Accessories",
            "description": "Logitech G502 gaming mouse",
            "storage": "",
            "model_number": "G502",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Logitech+G502"
        },

        {
            "name": "Razer DeathAdder",
            "brand": "Razer",
            "category": "Accessories",
            "description": "Razer DeathAdder gaming mouse",
            "storage": "",
            "model_number": "DeathAdder",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Razer+DeathAdder"
        },

        {
            "name": "Logitech K380",
            "brand": "Logitech",
            "category": "Accessories",
            "description": "Logitech K380 wireless keyboard",
            "storage": "",
            "model_number": "K380",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Logitech+K380"
        },

        {
            "name": "Logitech MX Keys",
            "brand": "Logitech",
            "category": "Accessories",
            "description": "Logitech MX Keys wireless keyboard",
            "storage": "",
            "model_number": "MX Keys",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=MX+Keys"
        },


        # =========================================================
        # CAMERAS
        # =========================================================

        {
            "name": "Canon EOS R50",
            "brand": "Canon",
            "category": "Camera",
            "description": "Canon EOS R50 mirrorless camera",
            "storage": "",
            "model_number": "EOS R50",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Canon+EOS+R50"
        },

        {
            "name": "Sony Alpha A6400",
            "brand": "Sony",
            "category": "Camera",
            "description": "Sony Alpha A6400 mirrorless camera",
            "storage": "",
            "model_number": "Alpha A6400",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Sony+A6400"
        },

        {
            "name": "Nikon Z50",
            "brand": "Nikon",
            "category": "Camera",
            "description": "Nikon Z50 mirrorless camera",
            "storage": "",
            "model_number": "Z50",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Nikon+Z50"
        },

        {
            "name": "GoPro HERO 13",
            "brand": "GoPro",
            "category": "Camera",
            "description": "GoPro HERO 13 action camera",
            "storage": "",
            "model_number": "HERO 13",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=GoPro+HERO+13"
        },


        # =========================================================
        # HOME APPLIANCES
        # =========================================================

        {
            "name": "Dyson V8",
            "brand": "Dyson",
            "category": "Home Appliance",
            "description": "Dyson V8 cordless vacuum cleaner",
            "storage": "",
            "model_number": "V8",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=Dyson+V8"
        },

        {
            "name": "Dyson V12",
            "brand": "Dyson",
            "category": "Home Appliance",
            "description": "Dyson V12 cordless vacuum cleaner",
            "storage": "",
            "model_number": "V12",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=Dyson+V12"
        },

        {
            "name": "Xiaomi Air Purifier 4",
            "brand": "Xiaomi",
            "category": "Home Appliance",
            "description": "Xiaomi Air Purifier 4",
            "storage": "",
            "model_number": "Air Purifier 4",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=Xiaomi+Air+Purifier"
        },

        {
            "name": "LG 7 KG Washing Machine",
            "brand": "LG",
            "category": "Home Appliance",
            "description": "LG 7 KG fully automatic washing machine",
            "storage": "",
            "model_number": "LG 7KG Washing Machine",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=LG+Washing+Machine"
        },

        {
            "name": "Samsung 7 KG Washing Machine",
            "brand": "Samsung",
            "category": "Home Appliance",
            "description": "Samsung 7 KG fully automatic washing machine",
            "storage": "",
            "model_number": "Samsung 7KG Washing Machine",
            "color": "Silver",
            "image_url": "https://placehold.co/400x400?text=Samsung+Washing+Machine"
        },

        {
            "name": "Crompton Ceiling Fan",
            "brand": "Crompton",
            "category": "Home Appliance",
            "description": "Crompton ceiling fan",
            "storage": "",
            "model_number": "Crompton Ceiling Fan",
            "color": "White",
            "image_url": "https://placehold.co/400x400?text=Crompton+Fan"
        },


        # =========================================================
        # KITCHEN APPLIANCES
        # =========================================================

        {
            "name": "Philips Air Fryer",
            "brand": "Philips",
            "category": "Kitchen Appliance",
            "description": "Philips air fryer",
            "storage": "",
            "model_number": "Philips Air Fryer",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Philips+Air+Fryer"
        },

        {
            "name": "Philips Trimmer",
            "brand": "Philips",
            "category": "Personal Care",
            "description": "Philips men's electric trimmer",
            "storage": "",
            "model_number": "Philips Trimmer",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Philips+Trimmer"
        },

        {
            "name": "Philips Hair Dryer",
            "brand": "Philips",
            "category": "Personal Care",
            "description": "Philips hair dryer",
            "storage": "",
            "model_number": "Philips Hair Dryer",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Philips+Hair+Dryer"
        },

        {
            "name": "Samsung Microwave Oven",
            "brand": "Samsung",
            "category": "Kitchen Appliance",
            "description": "Samsung microwave oven",
            "storage": "",
            "model_number": "Samsung Microwave",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=Samsung+Microwave"
        },

        {
            "name": "LG Microwave Oven",
            "brand": "LG",
            "category": "Kitchen Appliance",
            "description": "LG microwave oven",
            "storage": "",
            "model_number": "LG Microwave",
            "color": "Black",
            "image_url": "https://placehold.co/400x400?text=LG+Microwave"
        }

    ]


    # =============================================================
    # INSERT PRODUCTS
    # =============================================================

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