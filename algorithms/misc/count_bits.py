def count_bits(n):
  """count the number of bits set to 1 in n"""
  count = 0
  for i in xrange(0,32):
    if n & (1<<i):
      count += 1
  return count

for test in xrange(0,100):
  print "test: %d, %s, %s" % (test, bin(test), count_bits(test))

