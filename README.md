# learning algorithms, data structures, and design patterns

This is just a place for me to reaquaint myself with the theory and practice of computer science.

Also everything is in Python, because it's a langauge I want to get good at.

All code was written from scratch.

## Directories

in english

### Design Patterns

These come from *Head First Design Patterns*, which is all Java.

### Algorithms

These come from *Algorithms in a Nutshell, 2nd edition*. The code in the book is mostly Java with scattered Python showers.

### Learn Python the Hard Way

This is exactly what is sounds like. See http://learnpythonthehardway.org/ .

## Check spelling errors

Check spelling of all README.md files, they get placed in the sp_err/ directory.

```
mkdir -p sp_err
for file in **/README.md; do cat $file | aspell -a | grep -v '^*' >sp_err/`echo $file | sed 's,[/.],_,g'`; done
```

