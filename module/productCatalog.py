class ProductCatalog:
    def __init__(self):
        self.__products_by_id = {}
        self.__products_by_name = {}

    def view_product(self):
        return self.__products_by_id

    def add_product(self, product):
        if product not in self.__products_by_id and product not in self.__products_by_name:
            self.__products_by_id[product.get_id()] = product
            self.__products_by_name[product.get_name()] = product

    def modify_product(self, new_info, product):
        product.change_info(new_info)

    def delete_product(self, product):
        self.__products_by_id.pop(product.get_id())

    def remove_product(self, product_id):
        product_name = self.__products_by_id[product_id].get_name()
        del self.__products_by_id[product_id]
        del self.__products_by_name[product_name]

    def get_all_products(self):
        result = self.__products_by_id.items()
        return result

    def get_product_by_id(self, prod_id):
        return self.__products_by_id[prod_id]

    def get_product_by_name(self, prod_name):
        return self.__products_by_name[prod_name]

    def get_discounted_product(self, n=10, discount=0.1):
        products = []
        for key in self.__products_by_id:
            product = self.__products_by_id[key]
            if product.get_discount() >= discount:
                products.append(product)
                if len(products) >= n:
                    break
        return products

    def get_recommend_product(self):
        product = None
        for key in self.__products_by_id:
            product = self.__products_by_id[key]

        return product

    def get_recently_add_product(self, n = 9):
        products = []

        for key in self.__products_by_id:
            products.append(self.__products_by_id[key])

        return products[:-n-1:-1]
