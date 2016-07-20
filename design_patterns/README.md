# Design Patterns

The examples were all taken from *Head First Design Patterns*.

That book is written for Java, which makes some of the Python interpretations a bit wonkey. The top two culprits is no type constraints and no class interfaces. I've followed the code as accurately as I can, mostly with abstract methods, but the "interfaces" are more "hints of what is expected" than anything binding.

I suspect these translation problems would be found in all higher-level, interpreted languages, but I can only confirm it for Python and Perl.

## OO Design Principles

 - Encapsulate what varies.
 - Favor composition over inheritance.
 - Program to the interface, not the implementation.
 - Strive for loosely coupled designs between objects that interact.
 - Classes should be open for extension by closed for modification.
 - Depend on abstractions. Do not depend on concrete classes.
 - Only talk to your friends.
 - Don't call us, we'll call you.
 - A class should only have one reason to change.

## Related Patterns

### Factory Methods

Factories create objects. They make it easy for an application to get the object it needs.

 - **Factory Method** - Uses class inheritance to return the needed object. Used to create a single object.
 - **Abstract Factory** - Uses object composition to return the needed object. Used for creating families of objects (tons of related objects).

### Algorithms

 - **Strategy** - Creates a bunch of algorithms with composition, and lets the application pick one.
 - **Template** - Define a complete algorithm, and then let inherited subclasses change key steps.

### Wrappers

Some design patterns wrap objects for different reasons.

 - **Adaptor** - Wraps an object to make it look like a different object.
 - **Decorator** - Wraps an object to provide additional functionality.
 - **Facade** - Wraps an object to provide a simpler interface.
 - **Proxy** - Wraps an object to control and manage access to its interface.

### Changing behaviors

 - **Strategy** - Meant to change an object's behavior once.
 - **State** - Meant to change an object's behavior multiple times. Provides an structured transition between behaviors.

## Notes

 - Patterns that use inheritance can easily become more complicated.
 - Patterns that use composition can change at runtime.

