import re
from enum import Enum
from utilities import IdGenerator, Search
from module.productCatalog import ProductCatalog
from module.user import User, UserHolder
from module.publisher import Publisher


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


class Authenticator:
    @staticmethod
    def password_available(pass1, pass2):
        # one lowercase one uppercase one number one special character at least 8 char long
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if pass1 != pass2:
            return RegistStatus.PASSNOTMATCH
        elif not re.match(reg, pass1):
            return RegistStatus.PASSNOTSECURE
        return RegistStatus.PASSAVAILABLE

    @staticmethod
    def register(account_holder, kwargs):
        email = kwargs["email"]
        pass1 = kwargs["password2"]
        pass2 = kwargs["password2"]

        if account_holder.email_exist(email):
            print("Email already exist")
            return RegistStatus.EMAILALREADYEXIST
        pass_status = Authenticator.password_available(pass1, pass2)
        if pass_status == RegistStatus.PASSNOTMATCH:
            print("Password not match")
            return RegistStatus.PASSNOTMATCH
        elif pass_status == RegistStatus.PASSNOTSECURE:
            print("Password not secure must contain 1 lowercase, 1 uppercase, 1 number, 1 special character")
            return RegistStatus.PASSNOTSECURE

        return RegistStatus.SUCCESS

    @staticmethod
    def login(account_holder, email, password):
        if not account_holder.email_exist(email):
            return LoginStatus.EMAILNOTFOUND, None
        if not account_holder.password_correct(email, password):
            return LoginStatus.PASSNOTCORRECT, None

        return LoginStatus.SUCCES


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
        pass1 = kwargs["password2"]
        register_as = kwargs["register_as"]

        status = Authenticator.register(self.__account_holder, kwargs)

        if status != RegistStatus.SUCCESS:
            return status

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
        status = Authenticator.login(email, password)
        if status != LoginStatus.SUCCES:
            return status

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

    # ==== Search ====
    def search_profile(self, **kwargs):
        return Search.search_profile(self.__user_holder, kwargs)

    def search_product(self, search_name = ""):
        return Search.search_product(self.__product_catalog, search_name)

    # ================== About Board ================== #
    def get_board(self, board_name):
        return self.__community.get_board(board_name)
