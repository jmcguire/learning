#!/usr/bin/env python

import re

def build_match_apply_fns(pattern_group):
    pattern, search, replace = pattern_group
    match_fn = lambda noun: re.search(pattern, noun)
    apply_fn = lambda noun: re.sub(search, replace, noun)
    return (match_fn, apply_fn)

patterns = (('[sxz]$', '$', 'es'),
            ('[^aeioudgkprt]h$', '$', 'es'),
            ('[^aeiou]y$', 'y$', 'ies'),
            ('$', '$', 's'))

rules = [build_match_apply_fns(p) for p in patterns]

def plural(noun):
    for match_fn, apply_fn in rules:
        if match_fn(noun):
            return apply_fn(noun)

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

