#A [ (782,362,848,163,657,776,860,381,216,450,88,109,346,101,982,656,966,111,275,389,649,519,853,231,959,365,977,312,435,795]
A = [ 'b', 'f', 'c', 'd', 'a', 'e']

def show(A):
  print ", ".join(A)

# from 1 to length, place that element into the previous array
def insertion_sort(A):
  for i in range(0, len(A)):
    #print "starting at position %d" % i
    _insert_sort(A, i)
    #show(A)

# sort the element at start into the part of the array before it
def _insert_sort(A, start):
  for i in range(start, 0, -1):
    #print "  checking %d:%s and %d:%s" % (i, A[i], i-1, A[i-1])
    if A[i] < A[i-1]:
      #print "  %s < %s" % (A[i], A[i-1])
      A[i], A[i-1] = A[i-1], A[i]
    else:
      #print "  %s !< %s" % (A[i], A[i-1])
      break

show(A)
insertion_sort(A)
show(A)

