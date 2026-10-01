from .base_platform import BasePlatform
from .data_source_factory import (
    create_data_source
)


class BlinkitPlatform(BasePlatform):

    def __init__(self):

        self.name = "Blinkit"

        self.data_source = (
            create_data_source()
        )

    def search_product(
        self,
        product_name
    ):

        return self.data_source.search_product(

            self.name,

            product_name

        )