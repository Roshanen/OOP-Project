class Order:
    def __init__(self, id, total_price=0, date=None):
        self.__id = id
        self.__products = []
        self.__total_price = total_price
        self.__date = date

    def choose_method(system):
        return system.verify_payment()
