# Proxy

Provide a surrogate for an object.

## Problem

We have our GumballMachine, from the **State** pattern. Now we want to monitor it.

## Solution 1

We write a GumballMonitor, that takes in a GumballMachine, and reports on its data. Simple.

But that simple solution won't work remotely, it requires the machine and the monitor to live in the same process. What if we want to monitor the gumball machine from a remote computer?

## Proxy Pattern

We already have the GumballMonitor and the GumballMachine code written, so lets keep them as is. All we need is a "proxy" machine, that will live on the local computer but be connected to a gumball machine on a remote computer.

The **Proxy** is very similar to the **Decorator** pattern. The difference is the Decorator *adds* functionality, where the Proxy only *controls access* to existing functionality.

(Note that *Head First Design Principles* uses a very Java-specific solution. The python solution doesn't do remote-access, it just manages regular access.)

## OO Principle


