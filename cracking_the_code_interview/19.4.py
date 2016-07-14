# 19.4: given two numbers, determine the larger one with no if-statements or comparison operators

def cmp(m,n):
  """returns 1 if m > n, or -1 if m < n, or 0 if they are equal"""

  #print "%s cmp %s" % (bin(m), bin(n))
  
  i = 8 # bits in a number
  r = 0 # return value

  for i in range(8, -1, -1):
    # get the ith bit of the two numbers
    mi = (1<<i) & m
    ni = (1<<i) & n

    #print "%d bit: %s, %s" % (i, bin(mi), bin(ni))

    # fake a comparison using boolean operators
    r = r or (mi and not ni and 1) or (ni and not mi and -1)

  return r

# testing

#  5 is 0101
# 10 is 1010

print cmp(5,10)  # -1
print cmp(10,5)  # 1
print cmp(10,10) # 0 

