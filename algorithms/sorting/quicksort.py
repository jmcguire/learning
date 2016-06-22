# quicksort
#
# 1) pick a pivot element
# 2) move all the elements less than the pivot to the left of it, and larger
#    than to the right
# 3) now recursively quicksort our two "new" partitions on either side of the
#    pivot

def quicksort(A):
  _quicksort(A, 0, len(A) - 1)

def _quicksort(A, left, right):
  if left < right:
    pivot = pick_pivot(A, left, right)
    #print "from %d to %d, pivoting at %d (%s)" % (left, right, pivot, A[pivot])
    pivot = partition(A, left, right, pivot)
    #show(A)
    _quicksort(A, left, pivot - 1)
    _quicksort(A, pivot + 1, right)

def pick_pivot(A, left, right):
  return int((left + right) / 2) 

def partition(A, left, right, pivot):
  """move all elements < pivot to the left side, and > pivot to the right side"""
  A[right], A[pivot] = A[pivot], A[right]

  middle = left # middle points to where the numbers larger than the pivot begin
  for i in range(left, right):
    #print "checking %d, %d" % (i, middle)
    if A[i] <= A[right]: # right is where the pivot currently is
      A[i], A[middle] = A[middle], A[i]
      middle += 1

  # now we know that everything to the left of "middle" is less than the pivot
  #print "swapping %d (%s), %d (%s)" % (right, A[right], middle, A[middle])
  A[middle], A[right] = A[right], A[middle]
  return middle

