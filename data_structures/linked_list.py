class Node(object):
  """simple node for a linked list"""
  def __init__(self, e):
    self.next_ = None
    self.e = e

class LinkedList(object):
  """linked list with simple built-in iterator"""
  def __init__(self):
    self.first = None
    self.last = None
    self.current = None
    self.size = 0

  def next_(self):
    self.current = self.current.next_

  def reset(self):
    self.current = self.first

  def is_empty(self):
    if self.size == 0:
      return True
    else:
      return False

  def add_e(self, e):
    node = Node(e)
    self.add_node(node)

  def add_node(self, node):
    if self.is_empty():
      # our first node
      self.first = node
      self.last = node
      self.current = node
    else:
      self.last.next_ = node
      self.last = node

    self.size += 1

