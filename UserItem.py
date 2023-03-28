from datetime import datetime

class Item:
  def __init__(self, name = '', picture = '', got_date = '',description = '', status = '', amount = 0):
    self.__name = name
    self.__picture = picture
    self.__got_date = got_date
    self.__description = description
    self.__status = status
    self.__amount = amount

class Badge:
  def __init__(self, name = '', picture = '', got_date = '',description = '', status = ''):
    self.__name = name
    self.__picture = picture
    self.__got_date = got_date
    self.__description = description
    self.__status = status

class Factory:
  def __init__(self, product, user):
    self.__product = product
    self.__user = user
    self.__item_creator = ItemCreator()
    self.__badge_creator = BadgeCreator()

  def send_item(self, name, picture, got_date, description, status, amount):
    item = self.create_item(name, picture, got_date, description, status, amount)
    self.__user.add_item(item)

  def create_item(self, name, picture, got_date, description, status, amount):
    item = {'name ': name, 'picture': picture, 'got_date': got_date, 'description': description, 'status': status, 'amount': amount}
    return item
  
  def create_badge(self, name, picture, got_date, description, status):
    badge = {'name ': name, 'picture': picture, 'got_date': got_date, 'description': description, 'status': status}
    return badge

class ItemCreator(Factory):
  def __init__(self):
    pass

  def create_item(self, name, picture, got_date, description, status, amount):
    super().create_item(name, picture, got_date, description, status, amount)

class BadgeCreator(Factory):
  def __init__(self):
    pass

  def create_badge(self, name, picture, got_date, description, status):
    super().create_badge(name, picture, got_date, description, status)


date = datetime.now()
print(date.strftime("%Y-%m-%d %H:%M:%S"))