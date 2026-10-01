from flask import Flask, render_template

from config import Config
from models import db

from models.platform import Platform

from routes import products_bp

from services.product_seed import seed_products


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(products_bp)


@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# DATABASE SETUP
# ==========================================

with app.app_context():

    db.create_all()

    seed_products()

    if Platform.query.count() == 0:

        amazon = Platform(
            name="Amazon",
            website="https://www.amazon.in"
        )

        flipkart = Platform(
            name="Flipkart",
            website="https://www.flipkart.com"
        )

        blinkit = Platform(
            name="Blinkit",
            website="https://blinkit.com"
        )

        zepto = Platform(
            name="Zepto",
            website="https://www.zeptonow.com"
        )

        db.session.add_all([
            amazon,
            flipkart,
            blinkit,
            zepto
        ])

        db.session.commit()


# ==========================================
# START FLASK
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )