from module.shoppingCart import ShoppingCart
from utilities import IdGenerator
from module.order import Order
from module.library import Library
from module.chat import Chat
from module.purchaseHistory import PurchaseHistory

class User:
    def __init__(self, name, email, profile_picture="https://avatars.cloudflare.steamstatic.com/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb_full.jpg", description=None, level=0):
        self.__name = name
        self.__email = email
        self.__id = IdGenerator.generate_id(email)
        self.__profile_picture = profile_picture
        self.__description = description
        self.__level = level
        self.__friend_list = []
        self.__cart = ShoppingCart()
        self.__order = None
        self.__library = Library()
        self.__purchase_history = PurchaseHistory()
        self.__chat = Chat()
        self.__badge = []

    def __repr__(self):
        return self.__name

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def add_friend_list(self, user):
        self.__friend_list.append(user)
        
    def get_friend_list(self):
        return self.__friend_list
    
    def get_email(self):
        return self.__email

    def get_picture_profile(self):
        return self.__profile_picture

    def set_picture_profile(self, picture):
        self.__profile_picture = picture

    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_level(self):
        return self.__level

    def get_cart(self):
        return self.__cart

    def view_cart(self):
        return self.__cart.view_products()

    def add_to_cart(self, products):
        self.__cart.add_products(products)
        return self.__cart

    def get_library(self):
        return self.__library
    
    def get_purchase_hostory(self):
        return self.__purchase_history
    
    def get_chat(self):
        return self.__chat

    def request_item(self, factory):
        factory.check_condition(self)

    def add_badge(self, badge):
        if badge != None:
            self.__badge.append(badge)
            
    def create_order(self, product_list):
        order = Order(product_list)
