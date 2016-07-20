import pprint

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
    self.menu_items = []
    self.add_menu_item("Pancakes", "Regular pancakes", 2.99, True)
    self.add_menu_item("Trucker Pancakes", "Pancakes with eggs", 3.99, None)
    self.add_menu_item("Waffles", "Waffles with Maple Syrup", 4.99, True)
  def add_menu_item(self, name, desc, price, veggie):
    menu_item = MenuItem(name, desc, veggie, price)
    self.menu_items.append(menu_item)
  def get_menu_items(self):
    return self.menu_items

class Diner(object):
  """an collection based on an array, which is pretty hard to do in python"""
  def __init__(self):
    self.menu_items = [None,None,None,None,None,None]
    self.max_items = 6
    self.number_of_items = 0
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
  def get_menu_items(self):
    return self.menu_items

# testing      

if __name__ == '__main__':

  breakfast_menu = PancakeHouse()
  breakfast_items = breakfast_menu.get_menu_items()

  lunch_menu = Diner()
  lunch_items = lunch_menu.get_menu_items()

  def print_menu_item(menu_item):
    print "\t%s. %s -- %.2f" % (menu_item.get_name(), menu_item.get_desc(), menu_item.get_price())

  print "Breakfast Menu:"
  for menu_item in breakfast_items:
    print_menu_item(menu_item)

  print "\nLunch Menu:"
  for i in range(len(lunch_items)):
    if lunch_items[i] is None:
      continue
    menu_item = lunch_items[i]
    print_menu_item(menu_item)

