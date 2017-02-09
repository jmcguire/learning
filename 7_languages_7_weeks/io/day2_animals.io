Object ancestors := method(
    parent := self proto  
    if(parent != Object,
        writeln("Slots of ", parent type, "\n---------------")
        parent slotNames foreach(slotName, writeln(slotName))
        writeln
        parent ancestors))


Animal := Object clone
Animal speak := method(
            "ambiguous animal noise" println)

Duck := Animal clone
Duck speak := method(
            "quack" println)

Duck walk := method(
            "waddle" println)

disco := Duck clone
disco ancestors

