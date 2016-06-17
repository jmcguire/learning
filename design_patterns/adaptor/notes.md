# Adaptor

## Problem

We have a duck class that most of the code uses, but we now have a turkey class that we'd like to use with all our duck code.

(Also, anytime you have some legacy code that you want to be be compatible with newer code. Instead of rewriting the old code you can make an adaptor for it.)

## Solution 1

Rewrite the turkey class to be compatible with duck by adding a bunch of duck methods. Then inherit Duck from Turkey, which doesn't really make sense.

## Adaptor Pattern

Create a class that implements a duck using a turkey. Now that is a weird sentence.

Now there are two different ways to make an adaptor, which depend on whether you have multiple inheritance or not.

 - An *object adaptor* is used when you *don't* have multiple inheritance. The adaptor inherits from the target class, and instance of the adaptee class. So it IS-A duck and HAS-A turkey.
 - A *class adaptor* is used when you *do* have multiple inhertiance. The adaptor inherits from both the target and the adaptee class. So it IS-A duck and IS-A turkey.

## OO Principles

Coding to an interface. Since all our code expects the Duck interface (abstract class), we just have to make a compatible subclass.

