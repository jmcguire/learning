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


## COMMON OBJECT METHODS

    list.pop(0)
    list.pop(-1)
    list.append(...)
    string.split('...')

    'x'.join(list)


## IMPORTING AND IMPORTS

 - from
 - import
 - from ... import ...
 - from sys import argv
 - from sys import exit
 - from os.path import exists
 - argv
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


## COMMENT

    # basic comment

    def subname:
      """One-line comment about the function."""
      pass


