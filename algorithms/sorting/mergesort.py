
def show(A):
  print ", ".join(str(x) for x in A)

# mergesort:
# this is a version with a lot of function calls and array copies
# it demonstrates the general principle, but it does *not* work with just an extra O(n) space
# it needs to be refactored to use indexing in every function call, like quicksort

def mergesort(A):
  if len(A) < 2:
    return A

  elif len(A) == 2:
    if A[0] > A[1]:
      A[0], A[1] = A[1], A[0]
    return A

  else:
    # split up the array, and sort each half
    middle = len(A)/2
    left_A = mergesort(A[:middle])
    right_A = mergesort(A[middle:])
    # then merge it all back
    new_A = merge(left_A, right_A)
    return new_A

def merge(left_A, right_A):
  new_A = []
  left_i = 0
  right_i = 0
  while 1:
    if left_i >= len(left_A):
      # if we are out of left_A, append the rest of right_A to new_A
      new_A.extend(right_A[right_i:])
      break

    elif right_i >= len(right_A):
      # if we are out of right_A, append the rest of left_A to new_A
      new_A.extend(left_A[left_i:])
      break

    elif left_A[left_i] < right_A[right_i]:
      new_A.append( left_A[left_i] )
      left_i += 1

    elif left_A[left_i] >= right_A[right_i]:
      new_A.append( right_A[right_i] )
      right_i += 1

  return new_A

# testing

A = [ 'b', 'z', 'f', 'x', 'c', 'd', 'y', 'a', 'w', 'e']

show(A)
mergesort(A)
show(A)

#A = merge([1, 3, 6, 7], [0, 2, 4, 5, 8])
#show(A)
#A = merge([0, 1, 2, 3, 4], [5, 6, 7, 8])
#show(A)
#A = merge([5, 6, 7, 8], [0, 1, 2, 3, 4])
#show(A)

