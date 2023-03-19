class Product:
    def __init__(self,name,price,os_support,system_req,tags,cover_image,lang_sup,ban_country,exc_country,age_rate,discount,description,release_date):
        self.__name = name
        self.__price = price
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
    def add_to_wishlist(self,name):
        pass
    def add_to_cart(self,name,price,discount):
        pass