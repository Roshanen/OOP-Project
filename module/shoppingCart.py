class ShoppingCart:
    def __init__(self):
        self.__products = []

    def remove_all_product(self):
        self.__products = []

    def remove_product(self, product):
        self.__products.remove(product)

    def add_to_wishlist(self, product):
        pass

    def add_products(self, products):
        if products not in self.__products:
            self.__products.append(products)

    def get_products(self):
        return self.__products

    def calculate_total(self):
        price_sum = 0
        for product in self.get_products():
            price_sum += product.get_discounted_price()
        return price_sum
