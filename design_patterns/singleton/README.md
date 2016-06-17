# Singleton

## Problem

We want to ensure that only a single instance of an object exists, no matter who calls it or how many times it is called. Good for logging, database access.

## Solution 1

Use one global variable and instantiate it at the begining of your program.

## Singleton

Use a class with a private static variable. Every time the class is created, the internal of the class uses that one static variable.

(Note that Python doesn't have an easy implementation of the singleton. It can't use the Head First (Java) method because it can't prevent people from creating the class directly by make the constructor private.

## OO Design Principle


