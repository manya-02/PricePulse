## Project Structure

```text
PricePulse/
│
├── __pycache__/
│
├── instance/
│   └── pricepulse.db
│
├── logs/
│   └── pricepulse.log
│
├── models/
│   ├── __init__.py
│   ├── offer.py
│   ├── platform.py
│   └── product.py
│
├── routes/
│   ├── __init__.py
│   └── products.py
│
├── services/
│   ├── __init__.py
│   ├── amazon_platform.py
│   ├── api_config.py
│   ├── api_data_source.py
│   ├── api_response_handler.py
│   ├── api_response_parser.py
│   ├── base_platform.py
│   ├── blinkit_platform.py
│   ├── cache_service.py
│   ├── data_source.py
│   ├── data_source_factory.py
│   ├── flipkart_platform.py
│   ├── http_client.py
│   ├── logger.py
│   ├── mock_data_source.py
│   ├── mock_platform.py
│   ├── offer_matcher.py
│   ├── offer_service.py
│   ├── offer_validator.py
│   ├── platform_factory.py
│   ├── platform_manager.py
│   ├── platform_response.py
│   ├── platform_result.py
│   ├── platform_service.py
│   ├── price_service.py
│   ├── product_matcher.py
│   ├── product_seed.py
│   ├── product_service.py
│   ├── response_normalizer.py
│   └── zepto_platform.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── app.js
│       └── product.js
│
├── templates/
│   ├── index.html
│   └── product.html
│
├── venv/
│   └── ... (virtual environment files)
│
├── .env
├── .env.example
├── .gitignore
├── app.py
├── config.py
├── README.md
├── requirement.txt
├── requirements.txt
└── test_offer_matcher.py