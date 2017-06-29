Matrix := Object clone

Matrix dim := method(x, y, self x := x; self y := y; self l := list setSize(x * y))

Matrix set := method(x, y, value, if(x <= self x and y <= self y, l atPut(x*y, value), RAISEEXEPTION)

Matrix set := method(x, y, if(x <= self x and y <= self y, l at(x*y), RAISEEXEPTION)

Matrix transpose := method(
    
)


