# Observer

## Problem

We have one source of weather data, but a few different displays that need it. We have one class that will be called when appropriate (we don't know when, it's vendor-code). The only thing we can do is override the measurementchanged() function.

## Solution 1

Hardcode all the display classes into the weather data class, and manually call update() on each one.

## Observer Pattern

Let other classes (objects) "subscribe" to the weather data (subject). They can subscribe and unsubscribe. Each observer needs to implement an update() that the subject will call upon.

## OO Principle

Loose coupling.

