from module.user import User

class Publisher(User):
    def __init__(self, name, email, profile_picture="https://avatars.cloudflare.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg", level=0):
        super().__init__(name, email,profile_picture, level)
        self.__own_product = []

    def add_product(self, product):
        if product not in self.__own_product:
            self.__own_product.append(product)

    def remove_product(self, product_id):
        pass

    def get_all_own_products(self):
        return self.__own_product