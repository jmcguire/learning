#Observer Design Pattern

##Problem

A few different displays want to get weather data. We have one class that will be called when appropriate (we don't know when, it's vendor-code). the only thing we can do is override the measurements_changed() function.

##Solution 1

hardcode all the display classes into the weather data class, and manually call update() on each one

##Observer Pattern: 

let other classes (objects) "subscribe" to the weather data subject. Loose coupling.

