curlyBrackets := method(
    r := List clone
    call message arguments foreach(arg, r append(arg))
    r)

s := File with("day3_people.txt") openForReading contents
people := doString(s)
people println

