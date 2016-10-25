# binary search
#
# divide and conquer
# best time:    O(1)
# average time: O(logn)
# worst time:   O(logn)
#
# required a list of sorted elements
# look at the half-way mark, compare to e, move up or down, repeat

def binary_search(A, e, start=0, end=None):
  if end is None:
    end = len(A)-1

  middle = (start + end) // 2
  check = A[middle]
  
  #print "    start %d, end %d, middle %d (%s), prev_middle %s" % (start, end, middle, str(check), str(prev_middle))

  # check for failure
  if start > end:
    return False

  if e == check:
    return middle
  elif e > check:
    return binary_search(A, e, middle+1, end)
  elif e < check:
    return binary_search(A, e, start, middle-1)

# testing

def test(A, e):
  print "looking for", e
  position = binary_search(A, e)
  if position is not False:
    print " -> found item at", position
  else:
    print " -> did not find item"

A = range(1,100)

for e in xrange (0,101):
  test(A, e)

