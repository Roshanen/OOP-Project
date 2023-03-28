class ProductCatalog:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        self.__products[product.get_id()] = product