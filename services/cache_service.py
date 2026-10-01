from datetime import datetime, timedelta

from config import Config


def is_offer_fresh(offer):

    if not offer.last_updated:
        return False

    cache_duration = timedelta(
        minutes=Config.PRICE_CACHE_MINUTES
    )

    expiry_time = (
        offer.last_updated
        + cache_duration
    )

    return datetime.utcnow() < expiry_time


def get_fresh_offers(offers):

    fresh_offers = []

    for offer in offers:

        if is_offer_fresh(offer):
            fresh_offers.append(offer)

    return fresh_offers


def get_stale_offers(offers):

    stale_offers = []

    for offer in offers:

        if not is_offer_fresh(offer):
            stale_offers.append(offer)

    return stale_offers