## syntax

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

## logic

everything but *nil* and *false* evaluate to true. even 0.

`&& || and or`
 - short circuit execution

`& |`
 - non-short circuiting execution

## basic functions

puts foo # print with newline
print foo # print without newline

gets() get input from user

## objects

`foo.class`   # gives the class name
`foo.methods` # all methods on this object

### string methods

`.to_i` # convert to integer
`.to_a` # convert to ascii string

