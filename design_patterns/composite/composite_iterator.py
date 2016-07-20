from menu import MenuComponent, MenuItem, MenuComposite, create_test_data, Waitress

class MenuComponentIterator(object):
  """an iterator for MenuComponent"""
  def __init__(self, component):
    self.component = component
    self.i = 0
    self.sub_iter = None

  def __iter__(self):
    return self

  def next(self):

    # if we're in a submenu, continue handling it
    if self.sub_iter:
      try:
        return_ = self.sub_iter.next()
        return return_
      except StopIteration:
        self.sub_iter = None

    # check that we're still in bounds
    if self.i >= len(self.component.components):
      raise StopIteration()

    # get the next item
    item = self.component.get_child(self.i)
    self.i += 1

    # and handle it
    if isinstance(item, MenuItem):
      return item
    elif isinstance(item, MenuComposite):
      self.sub_iter = iter(item)
      return self.next()
    else:
      raise Exception("Something has gone terribly wrong.")


# teach MenuComponent how to iterate over itself

def menu_component_iter(self):
  return MenuComponentIterator(self)

MenuComponent.__iter__ = menu_component_iter


# give Waitress the ability to print a vegetarian menu

def print_veggie_menu(self):
  print "\nVegetarian Menu\n%s" % ("-" * 20)
  for item in self.menu:
    if item.is_veggie:
      item.print_()

Waitress.print_veggie_menu = print_veggie_menu

# testing

if __name__ == '__main__':
  restaurant_menu = create_test_data()
  waitress = Waitress(restaurant_menu)
  waitress.print_veggie_menu()

