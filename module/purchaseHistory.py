from module.order import Order

class PurchaseHistory:
    def __init__(self):
         self.__history_list = []
         
    def get_history_list(self):
        return self.__history_list
    
    def add_to_history(self, order):
        self.__history.append(order)
