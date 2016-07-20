# Abstract Factory

## Problem

We now want to franchise our pizza store (see Factory pattern), and let different stores pick which factory they want. Each factory produces a different style. There's a NY Style Pizza, Chicago Style Pizza, etc.

## Solution 1

Create the different factories, then each store has to load the factory and pass it to the store object.

## Factory Method Pattern

Put the pizza creation function back into the store class, but force subclasses to define it.

 - In the Factory Pattern, we have a concrete class that has all the non-changing (common) elements, and is given a factory that contains all the changing elements. It uses the factory to generate the correct object.
 - In Factory Method Pattern, we have an abstract class that is has all the non-changing elements, and it is subclassed wholly for the changing elements. Instead of having separate factory objects, we the factory is baked into the class itself.

## OO Principle

Encapsulation.

Depend on abstractions, not concrete classes.

