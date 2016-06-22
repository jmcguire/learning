# mergesort:
# this is a version with a lot of function calls and array copies
# it demonstrates the general principle, but it does *not* work with just an extra O(n) space
# it needs to be refactored to use indexing in every function call, like quicksort

def mergesort(A):
  new_A = list(A)
  _mergesort(new_A, A, 0, len(A) - 1)

def _mergesort(A, final, start, end):
  # A is the array to sort
  # final will hold the final sorted array
  # start and end are the starting and ending points on A (and final)

  #print "_mergesort: start: %d, end: %d" % (start, end)

  if end - start < 1:
    return

  elif end - start == 1:
    if final[end] < final[start]:
      final[end], final[start] = final[start], final[end]
    return

  else:
    # split up the array, and sort each half
    middle = (start + end) / 2
    _mergesort(final, A, start, middle)
    _mergesort(final, A, middle+1, end)
    # then merge it all back
    _mergesort_merge(A, final, start, middle, end)

def _mergesort_merge(A, final, start, middle, end):
  """merge A[start:middle] and A{middle+1:end] into final"""

  #print "start: %d, middle: %d, end: %d, array: %s" % (start, middle, end, ", ".join(str(x) for x in A[start:end+1]))

  # to make it more clear what we're doing, lets use better variable names
  final_idx = start
  left = start
  right = middle + 1

  while final_idx <= end:
    # there are only two options, either take a piece from the left side, or
    # take a piece from the ride side.

    #  - if left side is exhausted, take from the right
    #  - if right side is exhausted, take from the left
    #  - otherwise, compare the characters, and take the lowest

    # but to avoid duplicating code, we combine all these choices all into a
    # single complex if-else

    if left < middle + 1 and (right > end or A[left] < A[right]):
      final[final_idx] = A[left]
      final_idx += 1
      left += 1

    else:
      final[final_idx] = A[right]
      final_idx += 1
      right += 1

    #print "  left: %d, right: %d, final_idx: %d (%s)" % (left, right, final_idx, final[:final_idx])

