class BinaryNode(object):
  """a single node in a binary search tree"""
  def __init__(self, e):
    self.e = e
    self.left = None
    self.right = None
    self.parent = None

  def add(self, e):
    """add the new element in the appropriate place"""
    if e < self.e:
      if self.left is not None:
        self.left.add(e)
      else:
        node = BinaryNode(e)
        node.parent = self
        self.left = node
    else:
      if self.right is not None:
        self.right.add(e)
      else:
        node = BinaryNode(e)
        node.parent = self
        self.right = node

  def find_furthest_right(self):
    if self.right:
      return self.right.find_furthest_right()
    else:
      return self

  def find_furthest_left(self):
    if self.left:
      return self.left.find_furthest_left()
    else:
      return self

class BinarySearchTree(object):
  """mostly just holds the root node of a binary tree"""
  def __init__(self):
    self.root = None

  def add(self, new):
    if self.root is None:
      node = BinaryNode(new)
      self.root = node
    else:
      self.root.add(new)

  def __contains__(self, e):
    """a expressive alias for find()"""
    if self.find(e):
      return True
    else:
      return False

  def find(self, e):
    """return the node with e if it exists"""
    current = self.root

    while current is not None:
      if e == current.e:
        return current
      elif e < current.e:
        current = current.left
      elif e > current.e:
        current = current.right

    return False

  def rm(self, e):
    """remove the node with e, if it exists"""

    """ how to remove a node in a binary tree:
     we need three nodes:
      - parent: to_delete's parent
      - advance: to_delete's most rightmost node on it's left side (with no left children)
      - advance_parent: that node's parent

     if we're in the middle of a complicated tree, then we'll make three moves:
      1. advance takes the place of to_delete
      2. advance's right child is moved to advance_parent.left
      3. to_delete's children are moved to advance
    """

    to_delete = self.find(e)
    if not to_delete:
      raise Exception("error: can't remove, doesn't exist")
    parent = to_delete.parent

    # if there are no children, this will be easy
    if to_delete.left is None and to_delete.right is None:
      if parent is None: # it's a root node
        self.root = None
      elif parent.left == to_delete:
        parent.left = None
      elif parent.right == to_delete:
        parent.right = None
      else:
        raise Exception("parent doesn't think it's related to to_delete")
      return

    advance = None
    advance_parent = None

    # 2. find advance, and handle its child
    if to_delete.left is not None:
      advance = to_delete.left.find_furthest_right()

      advance_parent = advance.parent
      advance_parent.right = advance.left

      if advance.right:
        advance.right.parent = advance_parent.left

    elif to_delete.right is not None:
      advance = to_delete.right.find_furthest_left()

      advance_parent = advance.parent
      advance_parent.left = advance.right

      if advance.left:
        advance.left.parent = advance_parent.right

    else:
      raise Exception("to_delete suddenly has no children, but it did a minute ago")

    # 1. move advance to delete's spot
    advance.parent = to_delete.parent
    if parent is None:
      # we're a root node
      self.root = advance
    elif parent.left == to_delete:
      to_delete.parent.left = advance
    elif parent.right == to_delete:
      to_delete.parent.right = advance
    else:
      raise Exception("something has gone wrong")

    # 3. handle to_delete's children
    advance.left = to_delete.left
    advance.right = to_delete.right
    if to_delete.left:
      to_delete.left.parent = advance
    if to_delete.right:
      to_delete.right.parent = advance

  def show_all(self):
    """show all nodes, breadth-first"""
    nodes = []
    nodes.append(self.root)

    while nodes:
      node = nodes.pop(0) # basically, shift.
      print "node:", node.e,
      if node.parent:
        print "(parent: %s)" % str(node.parent.e),
      if node.left:
        print "- left: ", node.left.e,
        nodes.append(node.left)
      if node.right:
        print "- right:", node.right.e,
        nodes.append(node.right)
      print

  def show_all_visual(self, depth=0, node=None):
    """show all nodes, nicely formatted, depth-first"""
    indent = "  " * depth
    if node is None:
      node = self.root

    print "%s> %s" % (indent, node.e)

    if node.left:
      self.show_all_visual(depth+1, node.left)
    if node.right:
      self.show_all_visual(depth+1, node.right)

  # TODO

  def show_in_order(self):
    """left, current, right"""
    pass

  def show_post_order(self):
    """left, right, current"""
    pass

  def show_pre_order(self):
    """current, left, right"""
    pass

  def balance(self):
    pass

