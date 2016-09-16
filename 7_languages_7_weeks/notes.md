## loops

```
if foo
  stuff
end

unless foo
	stuff
end

while foo
	stuff
end

begin
	stuff
end while foo

until foo
	stuff
end

for foo in 1..10
  stuff
end
```

all of these except `for` can be used in suffix form, `stuff while foo`


## symbols

"foo" is a string, of the word foo
:foo is a symbol, identified with the word foo

All symbols with the same name are actually the same object.

"foo".object_id == "foo".object_id # false
:foo.object_id == :foo.object_id # true


## logic

everything but *nil* and *false* evaluate to true. even 0.

`&& || and or`
 - short circuit execution

`& |`
 - non-short circuiting execution


## functions

def foo
	stuff
end


## basic functions

```
puts foo # print with newline
print foo # print without newline

gets() # get input from user
```


## objects

basic syntax


```
class Foo
	attr_accessor :bar
	def initialize(bar)
		@bar = bar
	end
end
```

```
foo.class   # gives the class name
foo.superclass   # gives the parent class name
foo.methods # all methods on this object
foo.methods.include?(:bar) # does the foo object include the method bar
foo.object_id #  return a unique string that ids the object
```

### inheritance

 - Ruby uses single inheritance and mixins. Mixins are called "modules".
 - A module is defined like a class, but uses "module" instead of "class", and has a bunch of methods.
 - to include a mixin, add `include MixinName` at the top of the class.


## strings

```
3.times {stuff} # do stuff 3 times
foo.to_i # convert to integer
foo.to_a # convert to ascii string
```


## arrays

```
[].class
foo.push(bar)
foo.pop
foo.max
foo.sort # returns a new list, does not sort in place
foo.member?(bar) # returns true if bar is in foo
```

and execute code on the list


```
foo.each {|a| code} # execute the block for each item in foo
foo.any? {|a| code} # returns true if block returns true for any item in foo
foo.all? {|a| code} # returns true if block returns truee for all items in foo
foo.collect {|a| code} # executes block for each item, and returns the new list, **map**
foo.select {|a| code} # returns only the items in foo where block returns true
foo.inject {|total, i| code} # executes block repeatedly with each item, passing the last result into the next execution

```


## code blocks

if a code block is the last parameter of a function call, it doesn't have to be in parentheses.

`foo(2, {code})` is the same as `foo(2) {code}`

pass around code with &code. no idea why

		def foo(&code)
			code.call
		end

**yield** - a function can take in a code block, and call it in the middle of itself. a ruby-esque way to do that is to use the yield keyword. it means "even though we didn't take code as a parameter, execute the code block that followed the invocation of this function".

		def foo
			stuff
			yield
			stuff
		end

		foo {code}


