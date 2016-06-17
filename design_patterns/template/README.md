# Template

## Problem

We have coffee, and we have tea. Each one has it's own way of being prepared (it's own algorithm), but the algorithms are suspiciously similar.

## Solution 1

Just create two algorithms and manage them separetely.

## Template Pattern

Make one algorithm, put it in a super class, CaffeinatedBeverage. Make both coffee and tea both sub classes CaffeinatedBeverage. Let coffee and tea just redfine certain steps, not the entire algorithm.

**Jargon:** The methods that don't change in an algorithm are called *concrete operations*. The abstract methods that are expected/required to be overwritten are called *primitive operations*.

## OO Principle

Encapsulate a whole algorithm.

Hollywood Principle: "Don't call us, we'll call you." We depend on the CaffeineBeverage algorithm, not on anything in the concrete classes. The individual steps in Coffee and Tea aren't called by our ultimate code, just the prepare algorithm.

