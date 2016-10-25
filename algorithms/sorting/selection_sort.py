# selection sort
#
# type: transposition
# best time:    O(n²)
# average time: O(n²)
# worst time:   O(n²)
#
# find the highest element, and swap it with the last element
# repeat for length - 1, length - 2, etc

def selection_sort(A):
  # starting at the last element down to 0, see if there's an higher element, and swap it
  for i in xrange(len(A)-1, 0, -1):

    # first, find the maximum element
    max_element = i
    for j in xrange (0, i+1):
      if A[j] > A[max_element]:
        max_element = j

    #print "starting at %d: %s" % (i, A[i])
    #print "our maximum element is %d: %s" % (max_element, A[max_element])

    # swap the new maximum with the highest
    A[i], A[max_element] = A[max_element], A[i]

