from Community import *
from fuzzywuzzy import process
import re

class System:
    def __init__(self) -> None:
        self.__boards = []
        self.__product_catalog = {}
        self.__user_account = {} # email:password
        self.__user_by_id = {}
        self.__user_by_name = {}
        self.current_user = None

    def add_product(self,product):
        self.__product_catalog[product.get_name()] = product

    def add_user(self,user):
        self.__user_by_name[user.get_name()] = user
        self.__user_by_id[user.get_id()] = user

    def search_profile(self,**kwargs):
        # get id and name that user want to search
        search_id = kwargs["search_id"]
        search_name = kwargs["search_name"]

        if search_id:  # if there is id to search
            try:
                return self.__user_by_id[search_id]
            except KeyError:
                return None
        elif search_name:  # if there is name to search
            # the extract return tuple -> (str,similarity)
            found_user_name = process.extract(search_name, self.__user_by_name.keys())
            # keep the user that have similarity 55 percent or more
            found_user = [self.__user_by_name[user[0]] for user in found_user_name if user[1] >= 55]
            # if there occur some user
            if found_user:
                return found_user
        # if there are no id or name to search
        return None

    def search_product(self,search_name = ""):
        if search_name != "":
            found_product_name = process.extract(search_name, self.__user_by_name.keys())
            found_product = [self.__user_by_name[user[0]] for user in found_product_name if user[1] > 55]

            if found_product:
                return found_product

        return None

    def verify_payment(self):
        return True

    def verify_login(self,username,password):
        pass

    def register(self,**kwargs):
        email = kwargs["email"]
        pass1 = kwargs["pass1"]
        pass2 = kwargs["pass2"]
        user_name = kwargs["user_name"]

        if email in self.__user_account:
            return "email already exist"
        pass_status = self.verify_password(pass1,pass2)
        if pass_status == "not_match":
            return "password not match"
        elif pass_status == "not_secure":
            return "password not secure"

        self.__user_account[email] = pass1

        # user = User()
        # self.add_user(User)

        return True

    def verify_password(self,pass1,pass2):
        # use regex to check password
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if pass1 != pass2:
            return "not_match"
        elif not re.match(reg, pass1):
            return "not_secure"
        return True

    def generate_id(self):
        pass