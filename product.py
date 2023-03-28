class Product:
    def __init__(self, name, price, product_id, os_support=None, system_req=None, tags=None, cover_image=None, lang_sup=None, ban_country=None, exc_country=None, age_rate=None, discount=None, description=None, release_date=None):
        self.__info = {'name':name,'price':price}
        self.__name = name
        self.__price = price
        self.__product_id = product_id
        self.__os_support = os_support
        self.__system_req = system_req
        self.__tags = tags
        self.__cover_image = cover_image
        self.__lang_sup = lang_sup
        self.__ban_country = ban_country
        self.__exc_country = exc_country
        self.__age_rate = age_rate
        self.__discount = discount
        self.__description = description
        self.__release_date = release_date
        # catalog.add_product(self)

    def get_info(self, key):
        return self.__info[key]
    
    def get_name(self):
        return self.__info['name']

    def get_price(self):
        return self.__price
    
    def get_id(self):
        return self.__product_id