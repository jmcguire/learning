# test out a one dimensional array and the foreach loop
oda := list(1, 2, 3)
oda foreach(i, i println)

# add up a one dimensional array
n := 0
oda foreach(i, n = n + i); n println

# add up a two dimensional array
tda := list(list(1, 2, 3), list(4, 5, 6), list(7, 8, 9))
n := 0
tda foreach(inner, inner foreach(i, n = n + i)); n println

