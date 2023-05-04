import re
from fuzzywuzzy import process
from enum import Enum
from utilities import IdGenerator
from module.productCatalog import ProductCatalog
from module.user import User
from module.publisher import Publisher


class Search:
    @staticmethod
    def search_profile(user_holder, kwargs):
        # get id and name that user want to search
        found_user = []
        search_id = kwargs.get("search_id")
        search_name = kwargs.get("search_name")

        if search_id:  # if there is id to search
            return user_holder.get_user_by_id(search_id)

        elif search_name:  # if there is name to search
            # the extract return tuple -> (str,similarity)
            found_user_name = process.extract(search_name, user_holder.get_all_user_name())

            # keep the user that have similarity 55 percent or more
            found_user = [user_holder.get_user_by_name(user[0]) for user in found_user_name if user[1] >= 55]

        # if there are no id or name to search
        return found_user

    @staticmethod
    def search_product(product_catalog, search_name):
        if search_name != "":
            found_product_name = process.extract(search_name, product_catalog.get_all_products()["by_name"].keys())
            found_product = [product_catalog.get_product_by_name(product[0]) for product in found_product_name if
                             product[1] > 55]
            if found_product:
                return found_product
        return []

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


class Account:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password


class AccountHolder:
    def __init__(self):
        self.__user_account: list[Account] = []

    def add_account(self, account):
        self.__user_account.append(account)

    def email_exist(self, email):
        for account in self.__user_account:
            if email == account.get_email():
                return True
        return False

    def password_correct(self, email, password):
        for account in self.__user_account:
            if email == account.get_email():
                return password == account.get_password()


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


class System:
    def __init__(self, product_catalog: ProductCatalog, community, user_holder: UserHolder, account_holder:AccountHolder):
        self.__community = community
        self.__product_catalog = product_catalog
        self.__user_holder = user_holder
        self.__account_holder = account_holder
        self.__current_user = None

    # ==== Product ====
    def add_product(self, product):
        self.__product_catalog.add_product(product)

    def get_product(self,prod_id):
        return self.__product_catalog.get_product_by_id(prod_id)

    def modify_product(self, new_info, product_id):
        product = self.get_product(product_id)
        self.__product_catalog.modify_product(new_info, product)

    def get_discount_product(self, n = 10, discount = 0.1):
        return self.__product_catalog.get_discounted_product(n, discount)

    def get_recommend_product(self):
        return self.__product_catalog.get_recommend_product()

    # ==== User ====
    def __add_user(self,user):
        self.__user_holder.add_user(user)

    def get_current_user(self) -> User:
        return self.__current_user

    def add_to_cart(self, product, user):
        user.add_to_cart(product)

    def get_all_user(self):
        return self.__user_holder.get_all_user()

    # ????
    def verify_payment(self):
        return True

    # LOGIN and REGISTER
    def register(self,**kwargs):
        # kwargs have to have these fixed argument
        user_name = kwargs["user_name"]
        email = kwargs["email"]
        register_as = kwargs["register_as"]
        pass1 = kwargs["password2"]
        pass2 = kwargs["password2"]

        if self.__account_holder.email_exist(email):
            print("Email already exist")
            return RegistStatus.EMAILALREADYEXIST

        pass_status = self.password_available(pass1,pass2)
        if pass_status == RegistStatus.PASSNOTMATCH:
            print("Password not match")
            return RegistStatus.PASSNOTMATCH
        elif pass_status == RegistStatus.PASSNOTSECURE:
            print("Password not secure must contain 1 lowercase, 1 uppercase, 1 number, 1 special character")
            return RegistStatus.PASSNOTSECURE

        account = Account(email, pass1)
        self.__account_holder.add_account(account)

        if register_as == "user":
            user = User(user_name, email)
            self.__add_user(user)
        else:
            publisher = Publisher(user_name, email)
            self.__add_user(publisher)

        return RegistStatus.SUCCESS


    def login(self, email, password):
        if not self.__account_holder.email_exist(email):
            return LoginStatus.EMAILNOTFOUND, None
        if not self.__account_holder.password_correct(email, password):
            return LoginStatus.PASSNOTCORRECT, None

        # since user ID is a hash using email then we can hash the email to get user instead of ID
        user_id = IdGenerator.generate_id(email)
        login_user = self.__user_holder.get_user_by_id(user_id)
        self.__current_user = login_user

        return LoginStatus.SUCCES, login_user

    def logout(self):
        self.__current_user = None

    def is_logged_in(self):
        if self.__current_user is None:
            return False
        return True

    def password_available(self,pass1,pass2):
        # one lowercase one uppercase one number one special character at least 8 char long
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if pass1 != pass2:
            return RegistStatus.PASSNOTMATCH
        elif not re.match(reg, pass1):
            return RegistStatus.PASSNOTSECURE
        return RegistStatus.PASSAVAILABLE

    # ==== Search ====
    def search_profile(self, **kwargs):
        return Search.search_profile(self.__user_holder, kwargs)

    def search_product(self, search_name = ""):
        return Search.search_product(self.__product_catalog, search_name)

    # ================== About Board ================== #
    def get_board(self, board_name):
        return self.__community.get_board(board_name)
