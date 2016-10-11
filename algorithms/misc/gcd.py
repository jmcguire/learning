
def gcd(m, n):
  """greatest common denominator, with euclid"""
  if n > m:
    m, n = n, m

  r = m % n # get the remainder

  if r == 0:
    return n

  return gcd(n, r)


# testing

print gcd(100, 90) # 10
print gcd(24, 18) # 6
print gcd(55, 35) # 5
print gcd(1000,999) # 1

