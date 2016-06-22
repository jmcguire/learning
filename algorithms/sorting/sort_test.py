from mergesort import mergesort
from bubble import bubble_sort
from insertion import insertion_sort
from quicksort import quicksort
from selection import selection_sort

def show(A):
  print ", ".join(str(x) for x in A)

A = [ 'b', 'z', 'f', 'x', 'c', 'd', 'y', 'a', 'w', 'e']

show(A)
mergesort(A)
show(A)

