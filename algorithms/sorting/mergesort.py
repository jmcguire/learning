# mergesort:
#
# type: sorting with extra storage, stable
# best time:    O(n logn)
# average time: O(n logn)
# worst time:   O(n logn)
#
# split the list in half, sort those halfs individually, then merge the two
# halves together.
# how do we sort each half? by recursively calling mergesort on them, of
# course.

def mergesort(A):
  temp = list(A)
  _mergesort(A, temp, 0, len(A) - 1)

def _mergesort(A, temp, start, end):
  # A is the array to sort
  # start and end are the starting and ending points on A
  # (start and end are *inclusive* pointers)

  #print "_mergesort: start: %d, end: %d" % (start, end)

  if end - start < 1:
    return

  elif end - start == 1:
    if A[end] < A[start]:
      A[end], A[start] = A[start], A[end]
    return

  # split up the array, and sort each half
  middle = (start + end) / 2
  _mergesort(A, temp, start, middle)
  _mergesort(A, temp, middle+1, end)

  # then merge it all back
  _mergesort_merge(A, temp, start, middle, end)

def _mergesort_merge(A, temp, start, middle, end):
  """merge A[start:middle] and A{middle+1:end] into final"""

  #print "start: %d, middle: %d, end: %d, array: %s" % (start, middle, end, ", ".join(str(x) for x in A[start:end+1]))

  # to make it more clear what we're doing, lets use better variable names
  idx = start
  left = start
  right = middle + 1

  while idx <= end:
    # there are only two options, either take a piece from the left side, or
    # take a piece from the ride side.

    #  - if left side is exhausted, take from the right
    #  - if right side is exhausted, take from the left
    #  - otherwise, compare the characters, and take the lowest

    # but to avoid duplicating code, we combine all these choices all into a
    # single complex if-else

    if left < middle + 1 and (right > end or A[left] < A[right]):
      temp[idx] = A[left]
      idx += 1
      left += 1

    else:
      temp[idx] = A[right]
      idx += 1
      right += 1

    #print "left: %d, right: %d, idx: %d (%s)" % (left, right, idx, temp[:idx])

  # now copy temp back to A
  # (there is a way to avoid this step, by reversing A and temp in the
  # _mergesort recursive calls, but that complicates the learning.)
  for i in range(start,end+1):
    A[i] = temp[i]

