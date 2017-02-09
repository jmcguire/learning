// tail recursion is always so pretty
fibRecursion := method(n, i, j,
  if(i == nil,
     fibRecursion(n, 0, 1),
     if(n == 0,
        j,
        fibRecursion(n-1, j, j+i)
     )
  )
)

// so ugly
fibLoop := method(n,
  a := 1
  b := 1
  for(i, 1, n,
    c := b
    b := a + b
    a := c
  )
)

for(i, 1, 10,
  fibRecursion(i) println
  fibLoop(i) println
)

