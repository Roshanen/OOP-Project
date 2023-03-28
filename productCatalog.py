class ProductCatalog:
    def __init__(self):
        self.__products = {}

    def view_product(self):
        return self.__products

    def add_product(self, product):
        self.__products[product.get_id()] = product
    
    def modify_product(self, new_info, product_id):
        product = self.__products[product_id]
        product.change_info(new_info)
    
    def delete_product(self, product):
        self.__products.pop(product.get_id())