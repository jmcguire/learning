from menu import MenuComponent, MenuItem, MenuComposite, create_test_data

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
    if type(item) is MenuItem:
      return item
    elif type(item) is MenuComposite:
      self.sub_iter = iter(item)
      return self.next()
    else:
      raise Exception("Something has gone terribly wrong.")


# teach MenuComponent how to iterate over itself

def menu_component_iter(self):
  return MenuComponentIterator(self)

MenuComponent.__iter__ = menu_component_iter


# testing

if __name__ == '__main__':
  restaurant_menu = create_test_data()

  for item in restaurant_menu:
    item.print_()

