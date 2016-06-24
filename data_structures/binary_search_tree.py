class BinaryNode(object):
  """a single node in a binary search tree"""
  def __init__(self, e):
    self.e = e
    self.left = None
    self.right = None

  def add(self, e):
    """add the new element in the appropriate place"""
    if e < self.e:
      if self.left is not None:
        self.left.add(e)
      else:
        node = BinaryNode(e)
        self.left = node
    else:
      if self.right is not None:
        self.right.add(e)
      else:
        node = BinaryNode(e)
        self.right = node

class BinaryTree(object):
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
    """does the tree contain the value e"""
    current = self.root

    while current is not None:
      if e == current.e:
        return True
      elif e < current.e:
        current = current.left
      elif e > current.e:
        current = current.right
    return False

  def show_all(self):
    """show all nodes, breadth-first"""
    nodes = []
    nodes.append(self.root)

    while nodes:
      node = nodes.pop(0) # basically, shift.
      print "node:", node.e,
      if node.left:
        print "- left: ", node.left.e,
        nodes.append(node.left)
      if node.right:
        print "- right:", node.right.e,
        nodes.append(node.right)
      print

  def show_all_visual(self, depth=0, node=None):
    """show all nodes, nicely formatted"""
    indent = "  " * depth
    if node is None:
      node = self.root

    print "%s> %s" % (indent, node.e)

    if node.left:
      self.show_all_visual(depth+1, node.left)
    if node.right:
      self.show_all_visual(depth+1, node.right)
