from queue import Queue

q = Queue()
q.push_e('q')
print "queue size:", q.size
print

n = q.shift()
print "shifted off the letter", n.e
print "queue size:", q.size
print

q.push_e('w')
q.push_e('e')
q.push_e('r')
print "added three elements, queue size:", q.size
print

q.push_e('t')
q.shift()
print "added and shifted an element, queue size:", q.size
print

for i in range(0,q.size):
  n = q.shift()
  print "shifted off the letter", n.e
  print "queue size:", q.size

