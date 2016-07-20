# Simple Factory

## Problem

We have a pizza store that makes a lot of different types of pizzas. There are two pieces to this, deciding what type of pizza to make, and then the preparation. The preparation is always the same, but the types of pizza we offer will keep changing.

## Solution 1

Add all the pizza types to a giant if-else statement. Modify as needed.

## Simple Factory Pattern

Remove all the pizza types from the PizzaStore. Instead have a single call to a factory, which will do that deciding for us. The stuff that doesn't change, the prep, stays in the PizzaStore.

## OO Principle

Encapsulation.

All factory patterns encapsulate object creation.

