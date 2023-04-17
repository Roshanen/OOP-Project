from datetime import datetime

class Item:
  def __init__(self, name='', picture='', description='', status='', amount=0, got_date=None):
    self.name = name
    self.picture = picture
    self.description = description
    self.status = status
    self.amount = amount
    if got_date is None:
      self.got_date = datetime.now()
    else:
      self.got_date = got_date

class Badge:
  def __init__(self, name='', picture='', description='', status='', got_date=None):
    self.name = name
    self.picture = picture
    self.description = description
    self.status = status
    if got_date is None:
      self.got_date = datetime.now()
    else:
      self.got_date = got_date

class Factory:
  def __init__(self, product, user):
    self.product = product
    self.user = user
    self.item_creator = ItemCreator()
    self.badge_creator = BadgeCreator()

  def send_item(self, name, picture, description, status, amount, got_date=None):
    item = self.item_creator.create_item(name, picture, description, status, amount, got_date)
    self.user.add_item(item)

  def send_badge(self, name, picture, description, status, got_date=None):
    badge = self.badge_creator.create_badge(name, picture, description, status, got_date)
    self.user.add_badge(badge)

class ItemCreator:
  def create_item(self, name, picture, description, status, amount, got_date=None):
    item = Item(name, picture, description, status, amount, got_date)
    return item

class BadgeCreator:
  def create_badge(self, name, picture, description, status, got_date=None):
    badge = Badge(name, picture, description, status, got_date)
    return badge