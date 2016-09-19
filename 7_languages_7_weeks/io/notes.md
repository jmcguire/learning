# Io

 - Everything is an object.
 - everything is messages and recievers.

## Messages

`reciever message` - pass the message tot he reciever


## Objects

:Prototype Objects: Objects are created by cloning, not by classes. There are no classes.

Objects keep track of what it was cloned from. If it can't respond to a message, it passed the message to it's ancestor.

Objects have slots. Each slot can hold an object. (And since everything is an object, a lost can hold anything.)


  	Vehicle := Object clone # pass the message `clone` to `Object`, and assign it to `Vehicle`
  	Vehicle description := "something that moves" # create a new slot, and assign it a string
  	Vehicle description = "something that moves you" # reassign a slot


### Nomenclature

`InitialCapsObject := AnotherObject` - a new type of AnotherObject
`lowercaseobject := AnotherObject` - an "instance" (kinda) of AnotherObject, not a new type


### Common messages for objects


  	Foo slotNames 			# get all slots for this object (not its ancestors)
  	Foo type 						# get the type of this object. usually its name
  	Foo getSlot("name") # get the object in this slot (will go to the ancestors)
  	Foo proto 					# get the prototype (ancestor) information


### Misc

To see all the objects, call `Lobby`.

To make a singleton:

  	Highlander := Object clone
  	Highlander clone := Highlanger


## Methods

  	method("vroom" prinln) # create a method that prints "vroom" with a newline

## Lists

  	list("one", "two", 3)

Messages on a list

  	list (1,2,3) average
  	list (1,2,3) sum
  	list (1,2,3) at(n) # n is a number
  	list (1,2,3) append(foo)
  	list (1,2,3) pop
  	list (1,2,3) prepend(foo)
  	list (1,2,3) isEmpty

## Maps

  	foo := Map clone

Messages on a map

  	foo atPut("key", "value")
  	foo at("key")
  	foo asObject # return the keys and values
  	foo asList # a list of lists, where each inner list is (key, value)
  	foo keys
  	foo size # number of keys

## Logic

0 is true
"" (the empty list) is true


