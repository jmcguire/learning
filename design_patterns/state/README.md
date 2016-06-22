# State

## Problem

We have a Gumball state machine. We want to add a new state to it.

## Solution 1

In our first solution, the GumballMachine class contained all the user options, states, and state transitions. The user options were functions, and each function has a huge if-elif statement.

## State Pattern

We are going to refactor our GumballMachine. Each state will be an object, and it will contain the behavior for each possible user action. It's an inversion of our first solution, where each action contained behavior for each possible state.

The state pattern lets an object modify it's behaviors when its state changes.

It's very similar to a Strategy Pattern, but the State Pattern is built to modify behaviors at runtime, where the Strategy Pattern *can* do that too but isn't designed to.

## OO Principle

