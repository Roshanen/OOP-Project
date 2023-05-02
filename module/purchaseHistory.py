from module.order import Order


class PurchaseHistory:
    def __init__(self):
        self.__history_list = []
        self.__sorted_history = []

    def get_history_list(self):
        return self.__history_list

    def add_to_history(self, order):
        self.__history_list.append(order)
        self.add_to_sorted(order)
        
    def add_to_sorted(self, order):
        for product in order.get_products():
            self.__sorted_history.append([product, order.get_paid_date()])

    def get_sorted_history(self):
        return self.__sorted_history