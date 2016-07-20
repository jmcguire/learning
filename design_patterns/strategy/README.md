# Strategy

## Problem

We have this class, Duck, with a few behaviors (fly, quack, swim). There are child classes to duck, like Mallard and DecoyDuck, that may use each behavior differently, or may not use them at all.

## Solution 1

We could use inheritance, and each child class can override the behaviors. But this does not produce reusable code, some ducks may use the same type of behavior.

## Strategy Pattern

Move the behavior to separate objects, each Duck HAS-A behavior. Force the concrete child classes to choose the behaviors it wants in their own class initialization.

## OO Principle

Encapsulation.

