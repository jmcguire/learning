Builder := Object clone

# provide global indenting
_indent := 0
indent := method(
    for(i, 1, _indent, "    " print))

Builder forward := method(
    indent
    writeln("<", call message name, ">")
    _indent = _indent + 1

    call message arguments foreach(
        arg,
        content := self doMessage(arg);
        if(content type == "Sequence", indent; writeln(content)))

    _indent = _indent - 1
    indent
    writeln("</", call message name, ">"))

Builder ul(li("Self"), li("Io"), li("Javascript"))

