# Command

## Problem

We have a whole bunch of classes without any standardization. We want to control any or all of them from a single remote control.

## Solution 1

Create a remote control class, add every weird class into it. Add custom code to manage each one.

## Command Pattern

Create a wrapper for each weird class that, the wrapper does nothing but implement an "execute()" command. Then attach the command wrappers to our remote control class. The remote control class has slots (or a queue) to hold commands. Since it assumes they are all derived from the Command class, the remote control only needs to call execute().

All the weird stuff is hidden in the command objects.

**Terminology:** The remote control is the *Invoker*, and each weird class is a *Reciever*.

## OO Principles

Encapsulating the strange and frequently changing stuff behind a command object.

