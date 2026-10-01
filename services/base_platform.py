from abc import ABC, abstractmethod


class BasePlatform(ABC):

    name = ""

    timeout = 10

    @abstractmethod
    def search_product(self, product_name):
        """
        Search for a product and return
        standardized offer data.
        """
        pass