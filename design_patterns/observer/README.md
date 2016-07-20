# Observer

## Problem

We have one source of weather data, but a few different displays that need it. We have one class that will be called when appropriate (we don't know when, it's vendor-code). The only thing we can do is override the measurement-changed() function.

## Solution 1

Hard code all the display classes into the weather data class, and manually call update() on each one.

## Observer Pattern

Let other classes (objects) "subscribe" to the weather data (subject). They can subscribe and unsubscribe. Each observer needs to implement an update() that the subject will call upon.

## Terminology

 - **objects** - The watchers.
 - **subjects** - The thing being watched.
 - **subscribe** - When an object asks a subject to update the object about any changes.

## OO Principle

Loose coupling between objects that interact.

