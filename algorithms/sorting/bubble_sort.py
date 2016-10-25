# bubble sort:
#
# type: transposition
# best time:    O(n)
# average time: O(n²)
# worst time:   O(n²)
#
# look at each pair, if they're out of order then swap them
# go through the entire list twice

def bubble_sort(A):
  #print "from %d to %d" % (len(A)-1, 0)
  for i in xrange(len(A)-1, 0, -1):
    #print "  from %d to %d" % (0, i-1)
    for j in xrange(1, i+1):
      #print "    checking %d:%s and %d:%s" % (j, A[j], j-1, A[j-1])
      if A[j] < A[j-1]:
        #print "    %s < %s, swap" % (A[j], A[j-1])
        A[j], A[j-1] = A[j-1], A[j]
      #else: print "    %s !< %s" % (A[j], A[j-1])

