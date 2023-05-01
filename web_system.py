import re
from fuzzywuzzy import process
from enum import Enum
from utilities import IdGenerator
from module.productCatalog import ProductCatalog
from module.user import User

class LoginStatus(Enum):
    EMAILNOTFOUND = "e-mail not found"
    PASSNOTCORRECT = "password incorrect"
    SUCCES = "login success"

class UserStatus(Enum):
    GUEST = 0
    LOGEDIN = 1
    PUBLISHER = 2

class RegistStatus(Enum):
    EMAILALREADYEXIST = "e-mail already exist"
    PASSNOTMATCH = "password not match"
    PASSNOTSECURE = "password not secure"
    SUCCESS = "register success"
    PASSAVAILABLE = "password available"

class System:
    def __init__(self, product_catalog, community):
        self.__community = community
        self.__product_catalog = product_catalog
        self.__user_account = {}  # email:password
        self.__user_by_id = {}
        self.__user_by_name = {}
        self.__current_user = None

    def get_current_user(self):
        return self.__current_user

    def get_user_by_id(self, user_id):
        return self.__user_by_id[user_id]

    def get_all_user(self):
        return self.__user_by_id

    def add_product(self,product):
        self.__product_catalog.add_product(product)

    def get_product(self,prod_id):
        return self.__product_catalog.get_product_by_id(prod_id)

    def get_discount_product(self, n = 10, discount = 0.1):
        return self.__product_catalog.get_discounted_product(n, discount)

    def get_recommend_product(self):
        return self.__product_catalog.get_recommend_product()

    def __add_user(self,user):
        self.__user_by_name[user.get_name()] = user
        self.__user_by_id[user.get_id()] = user

    def verify_payment(self):
        return True

    # view profile
    def view_user_profile(self,user_id):
        user = self.__user_by_id[user_id]
        return user

    # LOGIN and REGISTER

    def register(self,**kwargs):
        # kwargs have to have these fixed argument
        user_name = kwargs["user_name"]
        email = kwargs["email"]
        pass1 = kwargs["password1"]
        pass2 = kwargs["password2"]

        if email in self.__user_account:
            print("Email already exist")
            return RegistStatus.EMAILALREADYEXIST

        pass_status = self.password_available(pass1,pass2)
        if pass_status == RegistStatus.PASSNOTMATCH:
            print("Password not match")
            return RegistStatus.PASSNOTMATCH
        elif pass_status == RegistStatus.PASSNOTSECURE:
            print("Password not secure must contain 1 lowercase, 1 uppercase, 1 number, 1 special character")
            return RegistStatus.PASSNOTSECURE

        self.__user_account[email] = pass1

        # this will add user to self.user
        user = User(user_name, email)
        self.__add_user(user)
        self.__current_user = user
        print("Register success")
        print(user.get_name(),user.get_id())
        return RegistStatus.SUCCESS

    def logout(self):
        self.__current_user = None

    def login(self,email,password):
        if email not in self.__user_account:
            print("Email not found")
            return LoginStatus.EMAILNOTFOUND, None
        elif password != self.__user_account[email]:
            print("Password incorrect")
            return LoginStatus.PASSNOTCORRECT, None

        print("Login success")
        # since user ID is a hash using email then we can hash the email to get user instead of ID
        login_user = self.__user_by_id[IdGenerator.generate_id(email)]
        self.__current_user = login_user

        return LoginStatus.SUCCES, login_user

    def password_available(self,pass1,pass2):
        # use regex to check password
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if pass1 != pass2:
            return RegistStatus.PASSNOTMATCH
        elif not re.match(reg, pass1):
            return RegistStatus.PASSNOTSECURE
        return RegistStatus.PASSAVAILABLE

    # Searching

    def search_profile(self,**kwargs):
        # get id and name that user want to search
        try:
            search_id = kwargs["search_id"]
        except KeyError:
            search_id = None
        try:
            search_name = kwargs["search_name"]
        except KeyError:
            search_name = None

        print("id",kwargs["search_id"])
        if search_id:  # if there is id to search
            try:
                return self.__user_by_id[search_id]
            except KeyError:
                return []
        elif search_name:  # if there is name to search
            # the extract return tuple -> (str,similarity)
            found_user_name = process.extract(search_name, self.__user_by_name.keys())
            # keep the user that have similarity 55 percent or more
            found_user = [self.__user_by_name[user[0]] for user in found_user_name if user[1] >= 55]
            # if there occur some user
            if found_user:
                return found_user
        # if there are no id or name to search
        return []

    def search_product(self,search_name="",):
        if search_name != "":
            found_product_name = process.extract(search_name, self.__product_catalog.get_all_products()["by_name"].keys())
            found_product = [self.__product_catalog.get_product_by_name(product[0]) for product in found_product_name if product[1] > 55]
            if found_product:
                return found_product
        return []

    def view_profile(self,user_id):
        return self.__user_by_id[user_id].get_info()

    def view_product(self,prooduct_id):
        return self.__product_catalog.get_product_by_id(prooduct_id)

    def modify_product(self,new_info, product_id):
        product = self.get_product(product_id)
        self.__product_catalog.modify_product(new_info, product)

    def add_to_cart(self, product, user):
        user.add_to_cart(product)

    # ================== About Board ================== #
    def get_board(self, board_name):
        return self.__community.get_board(board_name)
