from module.shoppingCart import ShoppingCart
from module.utilities import IdGenerator
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
        self.__wish_list = []
        self.__invite_list = []
        self.__pending_list = []
        self.__friend_list = []
        self.__cart = ShoppingCart()
        self.__order = None
        self.__library = Library()
        self.__purchase_history = PurchaseHistory()
        self.__chat = Chat(self)
        self.__badge = []

    def __repr__(self):
        return self.__name

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_invite_list(self):
        return self.__invite_list
    
    def add_invite_list(self, user):
        self.__invite_list.append(user)
        
    def clear_pending_list(self):
        self.__pending_list = []
        
    def remove_invite_list(self, user):
        self.__invite_list.remove(user)
        
    def clear_invite_list(self):
        self.__invite_list = []
        
    def get_pending_list(self):
        return self.__pending_list
    
    def add_pending_list(self, user):
        self.__pending_list.append(user)
        
    def remove_pending_list(self, user):
        self.__pending_list.remove(user)

    def add_friend(self, user):
        self.__friend_list.append(user)
        
    def remove_friend_list(self, user):
        self.__friend_list.remove(user)
        
    def get_friend_list(self):
        return self.__friend_list
    
    def get_email(self):
        return self.__email

    def get_profile(self):
        return self.__profile_picture

    def set_profile(self, picture):
        self.__profile_picture = picture

    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_level(self):
        return self.__level
    
    def level_up(self):
        self.__level += 1
        
    def get_wish_list(self):
        return self.__wish_list
    
    def add_wish_list(self, product):
        self.__wish_list.append(product)
        
    def remove_wish_list(self, product):
        self.__wish_list.remove(product)
        
    def clear_wish_list(self):
        self.__wish_list = []

    def get_cart(self):
        return self.__cart

    def view_cart(self):
        return self.__cart.get_products()

    def add_to_cart(self, products):
        self.__cart.add_products(products)
        return self.__cart

    def get_library(self):
        return self.__library
    
    def get_purchase_history(self):
        return self.__purchase_history
    
    def get_chat(self):
        return self.__chat

    def request_item(self, factory):
        factory.check_condition(self)

    def add_badge(self, badge):
        if badge != None:
            self.__badge.append(badge)
            
    def create_order(self, product_list=None):
        self.__order = Order(product_list)
        
    def get_order(self):
        return self.__order


class UserHolder:
    def __init__(self):
        self.__user: list[User] = []
        self.__all_id = []
        self.__all_user_name = []

    def add_user(self, user:User):
        self.__user.append(user)
        self.__all_id.append(user.get_id())
        self.__all_user_name.append(user.get_name())

    def get_user_by_name(self, user_name):
        for user in self.__user:
            if user.get_name() == user_name:
                return user

    def get_user_by_id(self, user_id):
        for user in self.__user:
            if user.get_id() == user_id:
                return user

    def get_all_user(self):
        return self.__user

    def get_all_user_id(self):
        return self.__all_id

    def get_all_user_name(self):
        return self.__all_user_name