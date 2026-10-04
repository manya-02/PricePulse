# PricePulse

PricePulse is a Python-based web application that compares product prices across multiple shopping platforms in one place.

It helps users search for products and quickly identify the lowest available price among different platforms.

## Features

- Product search
- Category-based product search
- Product matching
- Price comparison across multiple platforms
- Lowest-price detection
- Savings calculation
- Product details page
- Platform-wise offers
- Responsive web interface
- SQLite database
- Flask REST API
- Mock platform data for development and demonstration

## Platforms

PricePulse currently demonstrates price comparison across:

- Amazon
- Flipkart
- Blinkit
- Zepto

> The current version uses mock/demo pricing data. It does not claim to provide live prices or live inventory.

## Technologies Used

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

### Other Tools
- Git
- GitHub
- Python Virtual Environment

## How It Works

```text
User searches for a product
          ↓
     Product Matcher
          ↓
    Matching Products
          ↓
    Platform Offers
          ↓
    Price Comparison
          ↓
 Lowest Price + Savings
          ↓
       Results
