#!/usr/bin/env python

import re

def rules(lang):
    with open('rules.%s' % lang) as rules_file:
        for line in rules_file.readlines():
            pattern, search, replace = line.split()
            yield lambda noun: re.search(pattern, noun) and re.sub(search, replace, noun)

def plural(noun, lang="en"):
    for rule in rules(lang):
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

