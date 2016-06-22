from mergesort import mergesort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quicksort import quicksort
from selection_sort import selection_sort

import pprint

def show(A):
  pprint.pprint(A)

A = [ 'b', 'z', 'f', 'x', 'c', 'd', 'y', 'a', 'w', 'e']

show(A)
mergesort(A)
show(A)

