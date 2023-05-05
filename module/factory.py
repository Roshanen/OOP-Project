from datetime import datetime


class Badge:
    def __init__(self, name='', picture='', description='', min_level=0, min_product=0):
        self.__name = name
        self.__picture = picture
        self.__description = description
        self.__min_level = min_level
        self.__min_product = min_product
        self.__got_date = datetime.now()


class BadgeFactory:
    def __init__(self, all_badge):
        self.__all_badge = all_badge

    def verify_condition(self, user):
        for badge in self.__all_badge:
            if badge not in user.get_badge():
                if user.get_product_number() > badge.get_min_Level() != 0:
                    user.add_badge(badge)
                if user.get_product_number() > badge.get_min_product() != 0:
                    user.add_badge(badge)
