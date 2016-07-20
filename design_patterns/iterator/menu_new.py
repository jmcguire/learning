from abc import abstractmethod

# iterator classes

class Iterator(object):
  """abstract class for iterators"""
  @abstractmethod
  def has_next(self): pass
  @abstractmethod
  def get_next(self): pass

class PancakeIterator(Iterator):
  """concrete iterator for our pancake house, or any list-based collection"""
  def __init__(self, items):
    self.items = items
    self.pos = 0

  def has_next(self):
    if self.pos < len(self.items):
      return True
    else:
      return False

  def get_next(self):
    if self.pos < len(self.items):
      item = self.items[self.pos]
      self.pos += 1
      return item
    else:
      raise Exception("iterator is out of bounds: %d" % self.pos)

class DinerIterator(Iterator):
  """concrete iterator for our diner, or any array-based collection"""
  def __init__(self, items):
    self.items = items
    self.pos = 0

  def has_next(self):
    if self.pos < len(self.items) and self.items[self.pos] is not None:
      return True
    else:
      return False

  def get_next(self):
    if self.pos < len(self.items) and self.items[self.pos] is not None:
      item = self.items[self.pos]
      self.pos += 1
      return item
    else:
      raise Exception("iterator is out of bounds: %d" % self.pos)

# general-use classes

class MenuItem(object):
  def __init__(self, name, desc, veggie, price):
    self.name = name
    self.desc = desc 
    self.veggie = veggie
    self.price = price
  def get_name(self): return self.name
  def get_desc(self): return self.desc
  def get_veggie(self): return self.veggie
  def get_price(self): return self.price

# incompatible collection classes

class PancakeHouse(object):
  """a collection based on a linked list"""
  def __init__(self):
    self.name = "Breakfast Menu"
    self.menu_items = []
    self.add_menu_item("Pancakes", "Regular pancakes", 2.99, True)
    self.add_menu_item("Trucker Pancakes", "Pancakes with eggs", 3.99, None)
    self.add_menu_item("Waffles", "Waffles with Maple Syrup", 4.99, True)

  def add_menu_item(self, name, desc, price, veggie):
    menu_item = MenuItem(name, desc, veggie, price)
    self.menu_items.append(menu_item)

  def get_iterator(self):
    iterator = PancakeIterator(self.menu_items)
    return iterator

class Diner(object):
  """an collection based on an array, which is pretty hard to do in python"""
  def __init__(self):
    self.menu_items = [None,None,None,None,None,None]
    self.max_items = 6
    self.number_of_items = 0
    self.name = "Lunch Menu"
    self.add_menu_item("Soup", "Soup of the Day", 3.29, True)
    self.add_menu_item("BLT", "Bacon, Lettuce, Tomato, with optional Mutton", 2.99, None)
    self.add_menu_item("Hot Dog", "World famously cheap-ass hot dog", 0.25, None)

  def add_menu_item(self, name, desc, price, veggie):
    if self.number_of_items < self.max_items:
      menu_item = MenuItem(name, desc, veggie, price)
      self.menu_items[self.number_of_items] = menu_item
      self.number_of_items += 1
    else:
      raise Exception("maximum number of items reached!")

  def get_iterator(self):
    iterator = DinerIterator(self.menu_items)
    return iterator

class Waitress(object):
  def __init__(self):
    self.menus = []

  def add_menu(self, menu):
    self.menus.append(menu)

  def print_menu(self):
    """loop thru our iterators to loop thru our menu items"""
    for menu in self.menus:
      print "\n%s:" % menu.name
      iterator = menu.get_iterator()
      while iterator.has_next():
        menu_item = iterator.get_next()
        print "\t%s. %s -- %.2f" % (menu_item.get_name(), menu_item.get_desc(), menu_item.get_price())


# testing      

if __name__ == '__main__':

  breakfast_menu = PancakeHouse()
  lunch_menu = Diner()

  waitress = Waitress()
  waitress.add_menu(breakfast_menu)
  waitress.add_menu(lunch_menu)

  waitress.print_menu()

