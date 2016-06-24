from binary_search_tree import BinaryTree
from random import randint, shuffle

# small tree

bt = BinaryTree()
bt.add('a')
bt.add('d')
bt.add('e')
bt.add('f')
bt.add('b')
bt.add('c')

bt.show_all()
bt.show_all_visual()

for e in ['a','b','g']:
  if e in bt:
    print "%s was found" % e
  else:
    print "%s was not found" % e

print

# big tree

bt2 = BinaryTree()

# get ~100 distinct random numbers from 1 to 1000
random_number_hash = {}
for i in range(0,100):
  random_number_hash[randint(0,1000)] = True
random_numbers = [e for e in random_number_hash.keys()]
shuffle(random_numbers)

for e in random_numbers:
  bt2.add(e)

bt2.show_all_visual()

