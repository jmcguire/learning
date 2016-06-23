# heapsort
# construct a "tree" in the array
# heapify the tree: each node is greater than it's children
# this will place the largest element at the far left, 0
# swap element 0 with the far right
# now repeat, while ignoring the far right element

def heapsort(A):
  _init_heap(A)
  for i in range(len(A)-1, 0, -1):
    # move the largest element to the end
    swap(A,0,i)
    # re-heapify to put the largest element at position 0
    _heapify(A, 0, i-1)

def _init_heap(A):
  # len(A)//2 - 1 is the highest parent that can exist in a heap
  for i in range(len(A)//2 - 1, -1, -1):
    _heapify(A, i, len(A)-1)

def _heapify(A, start, end):

  left = _left_child(start)
  right = _right_child(start)

  #_heapfy_debug(A, start, end)

  # now lets look at the parent and it's two children. we'll find the largest
  # child and swap it with the parent, then reheapify that child's heap.

  larger = start

  if left <= end and A[left] > A[start]:
    larger = left
  if right <= end and A[right] > A[left] and A[right] > A[left]:
    larger = right

  if larger != start:
    swap(A, start, larger)
    _heapify(A, larger, end)

# this function is quite common in algorithms
def swap(A, i, j):
  A[i], A[j] = A[j], A[i]

# some simple functions to show how the heap structure works
def _left_child(i):
  return 2*i + 1
def _right_child(i):
  return 2*i + 2
def _parent(i):
  return (i - 1)//2

def _heapfy_debug(A, start, end):
  left = _left_child(start)
  right = _right_child(start)
  print "_heapify: from %d to %d, A: %s" % (start, end, ", ".join(str(x) for x in A[:end+1]) )
  print "  parent %s" % str(A[start]),
  if left <= end:
    print ", left %s" % str(A[left]),
  if right <= end:
    print ", right %s" % str(A[right]),
  print

