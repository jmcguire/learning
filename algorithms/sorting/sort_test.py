from mergesort import mergesort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quicksort import quicksort
from selection_sort import selection_sort
from heapsort import heapsort

import pprint

def show(A):
  pprint.pprint(A)

A = [ 'b', 'z', 'f', 'x', 'c', 'd', 'y', 'a', 'w', 'e']
#A = [ 5, 2, 1, 4, 6, 3 ]
#A = [1,2,3,4,5,6,7]

show(A)
heapsort(A)
show(A)

