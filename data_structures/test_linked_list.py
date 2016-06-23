from linked_list import LinkedList, Node

def show_all(ll):
  ll.reset()
  for i in range(0,ll.size):
    n = ll.current
    print "position %d element %s" % (i, str(n.e))
    ll.next_()

ll = LinkedList()
ll.add_e('q')
ll.add_e('w')
ll.add_e('e')
ll.add_e('r')
ll.add_e('t')

node = Node('y')
ll.add_node(node)

show_all(ll)

