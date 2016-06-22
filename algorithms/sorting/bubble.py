#A = [782,362,848,163,657,776,860,381,216,450,88,109,346,101,982,656,966,111,275,389,649,519,853,231,959,365,977,312,435,795]
A = [ 'b', 'f', 'c', 'd', 'a', 'e']

def show(A):
  print ", ".join(A)

# from 1 to length, place that element into the previous array
def bubble_sort(A):
  #print "from %d to %d" % (len(A)-1, 0)
  for i in range(len(A)-1, 0, -1):
    #print "  from %d to %d" % (0, i-1)
    for j in range(1,i):
      #print "    checking %d:%s and %d:%s" % (j, A[j], j-1, A[j-1])
      if A[j] < A[j-1]:
        #print "    %s < %s, swap" % (A[j], A[j-1])
        A[j], A[j-1] = A[j-1], A[j]
      #else: print "    %s !< %s" % (A[j], A[j-1])
    #show(A)

show(A)
bubble_sort(A)
show(A)

