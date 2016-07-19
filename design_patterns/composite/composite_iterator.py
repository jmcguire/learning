from menu import MenuComponent, MenuItem, MenuComposite, Waitress

class MenuComponentIterator(object):
  """an iterator for MenuComponent"""
  def __init__(self, component):
    self.component = component
    self.i = 0
    self.sub_iterator = None

  def __iter__(self):
    return self

  def next(self):

"""

the iterator has i, the ith element of menucomponent
the iterator has sub_iterator, which means we're working with a submenu

if we have a subiterator:
  if subiterator has another element:
    return it
  if we catch a StopIteration:
    clear the sub_iterator
    continue with rest of this function

if i < max_element
  raise StopIteration()

grab the ith element

increment i

if the element is an item:
  return the item
if the element is a composite:
  create an iterator for it
  set our sub_iterator
  call self.next


"""


# teach MenuComponent how to iterate over itself

def menu_component_iter(self):
  return MenuComponentIterator(self)

class MenuComponent.__iter__ = menu_component_iter


# testing

if __name__ == '__main__':
  restaurant_menu = create_test_data()

  for item in restaurant_menu:
    item.print_()

