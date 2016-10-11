from random import randint

def fisher_yates_shuffle(a):
    #print "for %d to 1" % len(a)
    for i in xrange(len(a), 1, -1):
        next_pos = randint(0, i-1)
        #print "swapping %d and %d" % (i-1, next_pos)
        a[i-1], a[next_pos] = a[next_pos], a[i-1]

    return a

if __name__ == '__main__':
    a = range(1, 10)
    print fisher_yates_shuffle(a)

