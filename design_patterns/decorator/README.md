# Decorator

## Problem

We have an object that will have some unknown number of modifications to it, but all those modifications will affect a specific part of the object. Like the display(), or the cost().

## Solution 1

Hard code the variables for all possible modifications.

## Decorator Pattern

Each modification is a class that layers on top of the original object. So when you call the basic functionality of the core class any of the decorator classes can call the super() function, then modify it, and poss it on.

A Window decorator might be things like ScrollBars and CloseButton. A Coffee decorator might be things like SoyMilk and Whip.

## OO Principle

Open for extension, closed for modification.

