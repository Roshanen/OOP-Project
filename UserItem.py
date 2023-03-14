class Item:
  def __init__(self, description = '', from_game = ''):
    self.__description = description
    self.__from_game = from_game

class Badge:
  def __init__(self, name, picture = '', description = '', status = ''):
    self.__name = name
    self.__picture = picture
    self.__description = description
    self.__status = status

class Factory:
  def __init__(self, product, user):
    self.__product = product
    self.__user = user
    self.__item_creator = ItemCreator()
    self.__badge_creator = BadgeCreator()

  def send_item(self):
    #pass
    pass

  def create_item(self):
    pass

class ItemCreator:
  def __init__(self):
    pass

  def create_item(self):
    pass

class BadgeCreator:
  def __init__(self):
    pass

  def create_badge(self):
    pass