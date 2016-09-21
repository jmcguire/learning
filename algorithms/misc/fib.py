
def fib(c):
  if c == 1: return 1
  if c == 2: return 1
  cur = 1
  last = 1
  for i in range(3,c): 
    cur, last = cur + last, cur
  return cur + last

# testing

for i in range(1,10):
  print fib(i)

