from linked_list import LinkedList, Node

class Queue(LinkedList):
  """a FIFO list"""

  # these two methods are just aliases for the regular LinkedList methods, but
  # are given the names we'd expect for a Queue
  def push_e(self, e):
    self.add_e(e)
  def push_node(self, node):
    self.add_node(node)

  def next_(self):
    """queues don't have a notion of next, the user only gets the first"""
    pass

  def shift(self):
    """return the first element of the list"""
    if self.size == 0:
      return None

    node = self.first
    self.first = node.next_
    self.size -= 1

    if self.is_empty():
      self.current = None
      self.last = None

    return node

