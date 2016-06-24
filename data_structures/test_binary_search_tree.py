from binary_search_tree import BinarySearchTree
from random import randint, shuffle

def check_for(bt, e):
  if e in bt:
    print "%s was found" % e
  else:
    print "%s was not found" % e

def load(bt):
  # a nicely balanced tree
  bt.add(10)
  bt.add(5)
  bt.add(2)
  bt.add(1)
  bt.add(4)
  bt.add(7)
  bt.add(6)
  bt.add(9)
  bt.add(15)
  bt.add(12)
  bt.add(11)
  bt.add(14)
  bt.add(17)
  bt.add(16)
  bt.add(19)

# small tree

if False:

  bt = BinarySearchTree()
  bt.add('a')
  bt.add('d')
  bt.add('e')
  bt.add('f')
  bt.add('b')
  bt.add('c')

  bt.show_all()
  bt.show_all_visual()

  for e in ['a','e','j']:
    check_for(bt,e)

  print

# deleting

if False:

  bt = BinarySearchTree()
  load(bt)
  bt.show_all_visual()

  print "\ndeleting leafless node 19"
  bt.rm(19)
  check_for(bt,19)
  bt.show_all_visual()

  print "\nreloading and deleting middle node 15"
  bt = BinarySearchTree()
  load(bt)
  bt.rm(15)
  bt.show_all_visual()

  print "\nreloading and deleting root node 10"
  bt = BinarySearchTree()
  load(bt)
  bt.rm(10)
  bt.show_all_visual()

# big tree

if False:

  bt2 = BinarySearchTree()

  # get ~100 distinct random numbers from 1 to 1000
  random_number_hash = {}
  for i in range(0,100):
    random_number_hash[randint(0,1000)] = True
  random_numbers = [e for e in random_number_hash.keys()]
  shuffle(random_numbers)

  for e in random_numbers:
    bt2.add(e)

  bt2.show_all_visual()

# huge tree

if False:

  bt2 = BinarySearchTree()

  # get ~10,000 distinct random numbers from 1 to 10,000,000
  random_number_hash = {}
  for i in range(0,10000):
    random_number_hash[randint(0,10000000)] = True
  random_numbers = [e for e in random_number_hash.keys()]
  shuffle(random_numbers)

  for e in random_numbers:
    bt2.add(e)

  # todo: look for one number
