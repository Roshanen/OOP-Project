from Order import *
from ShoppingCart import *
from Library import *
from System import *
import datetime

class User:
    def __init__(self, name, id, password, profile_picture=None, description=None, level=0) :
        self.__name = name
        self.__id = id
        self.__password = password
        self.__profile_picture = profile_picture
        self.__description = description
        self.__level = level
        self.__order = Order(self.__id)
        self.__cart = ShoppingCart(self.__id)
        self.__library = Library()
        mySystem.system_add_user(self)

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def get_cart(self):
        return self.__cart

    def view_cart(self):
        return self.__cart.view_products()
    
    def add_products(self, product):
        self.__cart.add_products(product)
        return self.__cart

    def get_library(self):
        return self.__library
