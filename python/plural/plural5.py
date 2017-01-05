#!/usr/bin/env python

import re

def build_match_apply_fns(pattern_group):
    pattern, search, replace = pattern_group
    return lambda noun: re.search(pattern, noun) and re.sub(search, replace, noun)

def plural(noun, lang="en"):
    with open('rules.%s' % lang) as rules_file:
        lines = rules_file.readlines()

    patterns = [l.split() for l in lines]
    rules = [build_match_apply_fns(p) for p in patterns]

    for rule in rules:
        result = rule(noun)
        if result:
            return result

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

