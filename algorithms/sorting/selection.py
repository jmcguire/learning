#A [ (782,362,848,163,657,776,860,381,216,450,88,109,346,101,982,656,966,111,275,389,649,519,853,231,959,365,977,312,435,795]
A = [ 'b', 'f', 'c', 'd', 'a', 'e']

def show(A):
  print ", ".join(A)

def selection_sort(A):
  # starting at the last element down to 0, see if there's an higher element, and swap it
  for i in range(len(A)-1, 0, -1):

    # first, find the maximum element
    max_element = i
    for j in range (0, i):
      if A[j] > A[max_element]:
        max_element = j

    #print "starting at %d: %s" % (i, A[i])
    #print "our maximum element is %d: %s" % (max_element, A[max_element])

    # swap the new maximum with the highest
    A[i], A[max_element] = A[max_element], A[i]

show(A)
selection_sort(A)
show(A)

