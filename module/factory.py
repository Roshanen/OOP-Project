import datetime


class Badge:
    def __init__(self, name='', picture='', description='', min_level=0, min_product=0):
        self.__name = name
        self.__picture = picture
        self.__description = description
        self.__min_level = min_level
        self.__min_product = min_product
        self.__got_date = None
        
    def get_name(self):
        return self.__name
    
    def get_picture(self):
        return self.__picture
    
    def get_description(self):
        return self.__description
    
    def get_min_level(self):
        return self.__min_level

    def get_min_product(self):
        return self.__min_product
    
    def set_got_date_today(self):
        self.__got_date = datetime.date.today()
    
    def get_got_date(self):
        return self.__got_date
        
class BadgeFactory:
    def __init__(self, all_badge):
        self.__all_badge = all_badge

    def verify_condition(self, user):
        for badge in self.__all_badge:
            if badge not in user.get_badges():
                if user.get_product_number() > badge.get_min_level() != 0:
                    badge.set_got_date_today()
                    user.add_badge(badge)
                if user.get_product_number() > badge.get_min_product() != 0:
                    badge.set_got_date_today()
                    user.add_badge(badge)
