import time

class Payment:
    def __init__(self,shopping_cart):
        self.__price = shopping_cart.products
        self.__status = "Not paid"
        self.__date_stamp = time.time()
        self.__payment_id = ""