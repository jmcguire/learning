#!/usr/bin/env python

# from C Anthony Risinger
# https://mail.python.org/pipermail/python-ideas/2015-February/032110.html

import itertools

class thing(str):
    n = itertools.count()

    def __new__(cls, *args, **kwds):
        self = super(thing, cls).__new__(cls, *args, **kwds)
        self.n = next(self.n)
        print '  LIFE! %s' % self.n
        return self

    def __del__(self):
        print '  WHY?  %s' % self.n

print '---constructor'
set_of_things = set([thing('hi'),thing('hi'),thing('hi')])

# reset, for the rest of the testing
thing.n = itertools.count()

print '---literal'
unused_set_of_things = {thing('hi'),thing('hi'),thing('hi')}

print '---one more'
set_of_things.add(thing('hi'))

print '---done'

