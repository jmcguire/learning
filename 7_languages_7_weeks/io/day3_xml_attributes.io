# xml builder

Builder := Object clone

Builder forward := method(
    attr := call message argAt(0);

    if(attr name == "curlyBrackets",
        writeln("<", call message name, call sender doMessage(attr) asXMLAttributes, ">"),
        writeln("<", call message name, ">"));

    call message arguments foreach(
        arg,
        if(attr type == "Map",
            attr = Object clone,
            content := self doMessage(arg);
              if(content type == "Sequence", writeln(content))))

    writeln("</", call message name, ">"))

Map asXMLAttributes := method(
    s := "";
    self keys foreach(k, s = s .. " " .. k .. "=\"" .. self at(k) .. "\"");
    s)


# create a mapping syntax from {"key": "value"}
# This works when I paste it into the REPL, but not when executed a file

OperatorTable addAssignOperator(":", "atPutValue")

Object curlyBrackets := method(
    r := Map clone;
    call message arguments foreach(arg, r doMessage(arg));
    r)

Map atPutValue := method(
    self atPut(
        call evalArgAt(0) asMutable removePrefix("\"") removeSuffix("\""),
        call evalArgAt(1))
)


# test
writeln

Builder ul(li("Self"), li("Io"), li("Javascript"))
writeln

Builder ul({"class": "prototypical"}, li("Self"), li("Io"), li("Javascript"))
writeln

