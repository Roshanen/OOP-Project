from product import Product

class Library:
    def __init__(self):
        self.__products = []

    def add_product(self, product_info):
        product = Product(product_info)
        self.__products.append(product)

    def get_products(self):
        return self.__products
    
    def view_products(self):
        return [product.get_name() for product in self.__products]
