# insertion sort
#
# type: transposition
# best time:    O(n)
# average time: O(n²)
# worst time:   O(n²)
#
# look at the element at i, move it backwards one by one until it's in the
# right place
# do this for i = 1 .. length of array

# from 1 to length, place that element into the previous array
def insertion_sort(A):
  for i in range(0, len(A)):
    #print "starting at position %d" % i
    _insert_sort(A, i)

# sort the element at start into the part of the array before it
def _insert_sort(A, right):
  for i in range(right, 0, -1):
    #print "  checking %d:%s and %d:%s" % (i, A[i], i-1, A[i-1])
    if A[i] < A[i-1]:
      #print "  %s < %s" % (A[i], A[i-1])
      A[i], A[i-1] = A[i-1], A[i]
    else:
      #print "  %s !< %s" % (A[i], A[i-1])
      break

