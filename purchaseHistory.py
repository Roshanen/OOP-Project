from order import Order

class purchaseHistory:
    def __init__(self):
         self.__history = []
         
    def get_history(self):
        return self.__history
    
    def add_to_history(self, Order):
        self.__history.append(Order)
