# Facade

## Problem

We have too many weird components that we would like to control through a single, simple interface.

In this case it's a slew of home theater components, that we would like to control with a single button.

## Solution 1

Create the components and adjust them one by one. And if we need to do this same thing in another place, copy it all over.

## Facaade Pattern

Create a class that contains all the component classes, and make a simple interface to control them all in one go.

## OO Principles

Encapsulation of weird stuff.

Principle of least knowledge. (or: Only talk to your friends, not your friends friends.) If our main code only interacts with the facade class, then it has fewer dependencies. Now whenever a component changes we only have to look at the facade class, nowhere else.

