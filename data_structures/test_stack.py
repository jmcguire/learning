from stack import Stack

s = Stack()
s.push_e('s')
print "stack size:", s.size
print

n = s.pop()
print "popped off the letter", n.e
print "stack size:", s.size
print

s.push_e('w')
s.push_e('e')
s.push_e('r')
print "pushed three elements, stack size:", s.size
print

s.push_e('t')
s.pop()
print "pushed and popped an element, stack size:", s.size
print

for i in range(0,s.size):
  n = s.pop()
  print "popped off the letter", n.e
  print "stack size:", s.size

