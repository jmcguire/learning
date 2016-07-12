# Design Patterns

The examples were all taken from *Head First Design Patterns*.

That book is written for Java, which makes some of the Python interpretations a bit wonkey. The top two culprits is no type constraints and no class interfaces. I've followed the code as accurately as I can, mostly with abstract methods, but the "interfaces" are more "hints of what is expected" than anything binding.

I suspect these translation problems would be found in all higher-level, interpreted languages, but I can only confirm it for Python and Perl.

## Wrappers

Some design patterns wrap objects for different reasons.

 - **Adaptor** - Wraps an object to make it look like a different object.
 - **Decorator** - Wraps an object to provide additional functionality.
 - **Facade** - Wraps an object to provice a simpler interface.
 - **Proxy** - Wraps an object to control and manage access to its interface.

