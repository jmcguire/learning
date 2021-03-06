# Io

 - Everything is an object.
 - Everything is messages and recievers.

## Messages

`<reciever> <message>` - pass the message to the reciever

Messages have three parts.

 - **Sender** - Who sent the message, often the surrounding method.
 - **Target** - Where the message is going, the receiver.
 - **Arguments** - Arguments, in the parentheses. These are *not* evaluated, just passed.

The `call` method gives introspection on messages.

    call sender
    call target
    call message arguments
    call message atArg(n)
    call message name

`doMessage(...)` evaluates/executes a message. Since everything is a message, this executes anything. Think eval.


## Objects

An object is just a collection of slots. Every object has a parent, called its prototype. If you access a slot on an object, and if it doesn't exist, it looks in its prototype.

:Prototype Objects: Objects are created by cloning, not by classes. There are no classes.

Objects keep track of what it was cloned from. If it can't respond to a message, it passes the message to its ancestor.

Objects have slots. Each slot can hold an object. (And since everything is an object, a slot can hold anything.)

Slot Assignment. `:=` assigns a new slot, `=` assigns to an existing slot.

    Vehicle := Object clone # pass the message `clone` to `Object`, and assign it to `Vehicle`
    Vehicle description := "something that moves" # create a new slot, and assign it a string
    Vehicle description = "something that moves you" # reassign a slot


### Nomenclature

 - `InitialCapsObject := AnotherObject` - a new type of AnotherObject
 - `lowercaseobject := AnotherObject` - an "instance" (kinda) of AnotherObject, not a new type

Both are objects. Only one is a type object.

### Common messages for objects

    Foo slotNames       # get all slots for this object (not its ancestors)
    Foo type            # get the type of this object. usually its name
    Foo getSlot("name") # get the object in this slot (will go to the ancestors)
    Foo proto           # get the prototype (ancestor)


### Misc

 - `Lobby` - All the objects in the global namespace.
 - `OperatorTable` - All operators.

To make a singleton:

    Highlander := Object clone
    Highlander clone := Highlander


## Methods

    method("vroom" println) # create a method that prints "vroom" with a newline

Everything except the last message is an argument. You can access those arguments in the last message.

    printAll := method(a, b, list(a, b) foreach(item, item println))
    printAll("justin", "carolyn")

### Lobby Methods

 - "text" println
 - writeln("text")

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
    foo values
    foo size # number of keys

## Logic

 - `0` is true
 - `""` (the empty list) is true


## Loops

    loop(...) # execute forever
    while(condition, code)
    
    for(variables, start, end, code)
    for(variables, start, end, jump, code)
    
    list_of_things foreach(thing, code)


## Conditionals

    if(conditional, code_for_true, code_for_false)
    if(conditional) then(code_for_true) else(code_for_false)

# Syntax

    ; separates statements - is required between statements in control constructs.

Note: In a file, a simple newline is all that's required to separate statements in a method. But if using the REPL, you need ;s.

    , separates arguments - in a method and control constructs

