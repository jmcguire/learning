from linked_list import LinkedList, Node

class Stack(LinkedList):
  """a LIFO list"""

  # these two methods are just aliases for the regular LinkedList methods, but
  # are given the names we'd expect for a Queue
  def push_e(self, e):
    self.add_e(e)
  def push_node(self, node):
    self.add_node(node)

  # our nodes only keep track of their next element, but a stack needs the Node
  # to keep track of the parent. instead of rewriting Node we'll just use next_
  # to mean parent.
  def add_node(self, node):
    if self.is_empty():
      # our first node
      self.first = node
      self.last = node
    else:
      node.next_ = self.last
      self.last = node
    self.size += 1

  def next_(self):
    """stacks don't have a notion of next, the user only gets the last"""
    pass

  def pop(self):
    """return the last element of the list"""
    if self.size == 0:
      return None

    node = self.last
    self.size -= 1

    self.last = node.next_

    if self.is_empty():
      self.current = None
      self.last = None
      self.first = None

    return node

