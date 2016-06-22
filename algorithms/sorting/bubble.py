
def show(A):
  print ", ".join(A)

# bubble sort:
# look at each pair, if they're out of order then swap them
# go through the entire list twice

def bubble_sort(A):
  #print "from %d to %d" % (len(A)-1, 0)
  for i in range(len(A)-1, 0, -1):
    #print "  from %d to %d" % (0, i-1)
    for j in range(1, i+1):
      #print "    checking %d:%s and %d:%s" % (j, A[j], j-1, A[j-1])
      if A[j] < A[j-1]:
        #print "    %s < %s, swap" % (A[j], A[j-1])
        A[j], A[j-1] = A[j-1], A[j]
      #else: print "    %s !< %s" % (A[j], A[j-1])
    #show(A)

# testing

A = [ 'b', 'z', 'f', 'x', 'c', 'd', 'y', 'a', 'w', 'e']

show(A)
bubble_sort(A)
show(A)

