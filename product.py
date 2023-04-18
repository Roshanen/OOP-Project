from utilities import IdGenerator
from community import Rating
class Product:
    def __init__(self, info):
            self.__info = {
            "id" : IdGenerator.generate_id(info["name"]),
            "name": info["name"],
            "price": info["price"],
            "os_support": info["os_support"],
            "system_req": info["system_req"],
            "pre_vid" : info["pre_vid"],
            "cover_image": info["cover_image"],
            "lang_sup": info["lang_sup"],
            "ban_country": info["ban_country"],
            "exc_country": info["exc_country"],
            "age_rate": info["age_rate"],
            "discount": info["discount"],
            "description": info["description"],
            "release_date": info["release_date"]
            }

            self.__rating = Rating()

    def __repr__(self):
        return self.__info["name"]

    def get_info(self):
        return self.__info

    def get_name(self):
        return self.__info['name']

    def get_cover(self):
        return self.__info["cover_image"]

    def get_price(self):
        return self.__info['price']
    
    def get_id(self):
        return self.__info['id']

    def get_discount(self):
        return self.__info["discount"]

    def get_rating(self):
        return self.__rating.get_rating()

    def change_info(self,new_info):
        for key in new_info:
            if new_info[key] != None:
                self.__info[key] = new_info[key]