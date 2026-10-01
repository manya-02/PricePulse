from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def search_product(
        self,
        platform_name,
        product_name
    ):
        """
        Return product data for a platform.
        """
        pass