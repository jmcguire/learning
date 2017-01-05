# Python

## BUILTINS AND BASICS

 - raw_input()
 - raw_input("...")
 - len(...)
 - len(string)
 - len(list)
 - hash(string)
 - =
 - True
 - False


 - [
 - ]
 - list = [...,...,...]
 - list[0]
 - list[3:5]
 - sort(list)
 - range(number)
 - range(number, number)
 - xrange(...)
 - enumerate(list)


## BRANCHING AND LOOPING

    while ... :
      ...

    for variable in list:
      ...

    while ... :
      continue ## goes to the next thing in the "while" of "for" loop

    if ... :
      ...
    elif ... :
      ...
    else:
      ...

Keywords:

 - break - break out of this loop
 - continue - continue at the top of the current loop

Weird branching and looping

    for foo in bar:
      ...
    else
      ... # this will happen once, after the for-loop is finished

How to break out of an inner loop

    for:               # outer loop
      for:            # inner loop
        if foo:
          break        # will break inner loop, and skip the else below
      else:
        continue      # if we didn't break, continue the outer loop
      break            # will break the outer loop



## DICTIONARY OBJECT

    dict_var = {
      'a': 'A',
      'b': 'B',
    }

    ['...'] # get or set the item

    foo.items() # return every key value pair (list of lists)

    foo.get(...) # get a value without creating it
    foo.get(..., ...) # return a default value if it doesn't exist


## COMPARISON OPERATORS

 - ==
 - <
 - >
 - <=
 - >=
 - !=
 - +=
 - in
 - and
 - or
 - not
 - is


## FUNCTIONS FOR STRINGS

    'x'.join(list)


## FUNCTIONS FOR LISTS

    list.pop(0)
    list.pop(-1)
    list.append(single_item)
    list.extend(list_of_items)
    string.split('...')
    string.split() # default to any amount of whitespace

    len(list) # not list.len()
    list.sort() # sorts in place


## FUNCTIONS FOR NUMBERS

    max(number)
    min(number)
    round(number, float_precision) # round(14.123, 1) == 14.1


## IMPORTING AND IMPORTS

 - from
 - import
 - from ... import ...
 - from sys import argv
 - from sys import exit
 - from os.path import exists
 - argv
 - argv[1] - the first command line argument
 - exists
 - exit(0)


## PRINTING

    print
    %

    print "%s %d %r" % (...)

    print string_one + string_two

    print """
    """

    print """
    """ % ...

    print '''
    '''

    print '.' * 10

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(...)


## STRING

    name += first_name + ' ' + last_name


## FILES

    file = open(filename)
    file.read()

    open(filename).read()

    open(filename, 'w')
    file.truncate()
    file.write(...)

    file.close()

    file.seek(0)

In actual use, use `with` to give context. With it, the file knows to close
itself when the context goes away.

    with open(filename, 'r') as file_in:
        # do stuff with file_in


## FUNCTIONS

 - def
 - return
 - *args


    def no_args():
      ...

    def two_args(arg1, arg2):
      ...

    def arbitrary_args(*args):
      arg1, arg2 = args
      ...

    def nothing_happens:
      pass


## OBJECTS

in general

    class MyObject(object):
      def __init__(self, variable_in):
        self.class_variable = variable_in
      def my_function(self, other_variable):
        ...

child objects

    class ChildObject(ParentObject):
      def parent_function(self):
        ...
        super(ChildObject, self).parent_function
        ...

super(object_name)


## MODULES

    import yaml
    yaml.load(file('file.yaml'))

to see your import path, which is modified by PYTHONLIB:

    import sys.path
    print sys.path


## COMMENT

    # basic comment

    def subname:
      """One-line comment about the function."""
      pass

## EXCEPTION HANDLING

    try:
        # do stuff
    except ExceptionType as err
        # do stuff with err


## PROCESS COMMAND LINE OPTIONS

    import sys
    import getopts

    try:
      opts, args = getopt.getopt(sys.argv[1:], 'hu:c:', ['user=', 'comment='])
    except getopt.GetoptError:
      print "%s [-h] [-u | -user <username>] [-c | -comment <comment_id>]" % sys.argv[0]
      sys.exit(2)

    for opt, arg, in opts:
      if opt in ['u', 'user']:
        get_user(arg)
      elif opt in ['c', 'comment']:
        get_comment(arg)
      elif opt == '-h':
        get_help()


## DISTRIBUTING PACKAGES

    python setup.py sdist
    python setup.py register pypi
    python setup.py sdist upload pypi


## REGULAR EXPRESSIONS

Regular expressions aren't as integrated as in Perl, but Python does give you a
regexp string type, `r'regexp'` to help. This string won't interpret anything in
the string. This lets you do stuff like `r'\1 \2 \\ comment'` without fear of an
unreadable amount of backslash escaping.

    import re

    # returns a match object, which evaluates to true or false in a boolean context (if statement)
    re.search(r'regexp', string)

    # returns new string
    # replaces globally by default
    new_string = re.sub(r'regexp_from', r'regexp_to', string)

## GENERATORS

Any function with a `yield` statement is a generator (a special purpose
coroutine). `yield` means returns a value, but maintains its state, and the next
time the function is called it will return to where the `yield` was called.

This whole thing is a way to lazily produce values.

    def get_primes(start, amount):
        """get amount number of primes, starting at start"""
        n = start
        while amount > 0
            if is_prime(n):
                amount -= 1
                yield n
            n += 1
    
    # get the first 10 primes
    primes = get_primes(1, 10)

    for prime in primes:
        print prime


In the above, `primes` is actually a generator object. The `for` statement just
calls `next(primes)` at every iteration, which returns to where `yield` left
off.

