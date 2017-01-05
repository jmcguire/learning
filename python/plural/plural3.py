#!/usr/bin/env python

import re

rules = ((
            lambda noun: re.search('[sxz]$', noun),
            lambda noun: re.sub('$', 'es', noun)
        ),(
            lambda noun: re.search('[^aeioudgkprt]h$', noun),
            lambda noun: re.sub('$', 'es', noun)
        ),(
            lambda noun: re.search('[^aeiou]y$', noun),
            lambda noun: re.sub('y$', 'ies', noun)
        ),(
            lambda noun: 1,
            lambda noun: noun + 's'
        ))

def plural(noun):
    for match, apply_ in rules:
        if match(noun):
            return apply_(noun)

if __name__ == '__main__':
    tests = [
        ('bird', 'birds'),
        ('fax', 'faxes'),
        ('rash', 'rashes'),
        ('cheetah', 'cheetahs'),
        ('candy', 'candies'),
        ('day', 'days'),
    ]

    for singular, pluralized in tests:
        result = plural(singular)
        if result == pluralized:
            print("yes, the plural of %s is %s" % (singular, result))
        else:
            print("no, the plural of %s should be %s, not %s" % (singular, pluralized, result))

