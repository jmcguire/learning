from abc import abstractmethod

# our new tree classes

class MenuComponent(object):
  """An abstract class to define an implementation"""
  @abstractmethod
  def print_(self): pass

  @abstractmethod
  def add(self, component): pass

  @abstractmethod
  def remove(self, component): pass

  @abstractmethod
  def get_child(self, i): pass


class MenuItem(MenuComponent):
  """a leaf node, of our menu tree"""
  def __init__(self, name, desc, price, is_veggie):
    self.name = name
    self.price = price
    self.desc = desc
    self.is_veggie = is_veggie

  def print_(self):
    # turn the boolean is_veggie into a print-friendly string
    veggie_string = ""
    if self.is_veggie:
      veggie_string = " (v)"

    print "\t%s. %s%s -- %.2f" % (self.name, self.desc, veggie_string, self.price)


class MenuComposite(MenuComponent):
  """a composite  node, that holds more MenuComponents"""
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.components = []

  def add(self, component):
    self.components.append(component)

  def remove(self, component):
    self.components.remove(component)

  def get_child(self, i):
    return self.components[i]

  def print_(self):
    print "\n%s: %s\n%s" % (self.name, self.desc, "-"*20)

    # python iterators interact with the for command, we don't have to
    # explicitly create and manage them, like in Java
    for component in self.components:
      component.print_()


# a simple waitress class, simpler than anything we had in "Iterator"

class Waitress(object):

  def __init__(self, menu):
    self.menu = menu

  def print_menu(self):
    self.menu.print_()
 
# testing

def create_test_data():
  pancake_house = MenuComposite("Breakfast", "Pancakes and breakfast items")
  cafe = MenuComposite("Lunch", "Classic cafe lunch items")
  dessert = MenuComposite("Dessert", "Simple desserts")

  pancake_house.add(MenuItem("Pancakes", "Regular pancakes", 2.99, True))
  pancake_house.add(MenuItem("Trucker Pancakes", "Pancakes with eggs", 3.99, None))
  pancake_house.add(MenuItem("Waffles", "Waffles with Maple Syrup", 4.99, True))

  cafe.add(MenuItem("Soup", "Soup of the Day", 3.29, True))
  cafe.add(MenuItem("BLT", "Bacon, Lettuce, Tomato, with optional Mutton", 2.99, None))
  cafe.add(MenuItem("Hot Dog", "World famously cheap-ass hot dog", 0.25, None))

  dessert.add(MenuItem("Apple Pie", "Homemade Grandma-approved apple pie", 1.59, True))
  dessert.add(MenuItem("Ice Cream", "Two scoops of our ice cream of the day", 1.00, True))
  cafe.add(dessert)

  restaurant_menu = MenuComposite("Restaurant Menu", "Welcome to our restaurant")
  restaurant_menu.add(pancake_house)
  restaurant_menu.add(cafe)

  return restaurant_menu

if __name__ == '__main__':

  restaurant_menu = create_test_data()
  waitress = Waitress(restaurant_menu)
  waitress.print_menu()

