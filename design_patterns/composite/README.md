# Composite

## Problem

(This builds on our work done with **Iterators.**)

We used to have a bunch of lists. We don't know how those lists are stored (linked lists, arrays, hash tables, etc), but we knew we'd need to access them all with the same way. We solved that problem by creating an iterator for each set with a simple, common interface.

Now we have a new problem. Some of our menus (lists) will have sublists. We still want a flexible way of handling it all, that includes a way to print out the entire menu, and a way to print out a specific menu.

At this point, we need to redo the menu. It needs to be *a tree.*

## Solution 1

We're building off our previous work from the **Iterators** pattern, so the "wrong" solution is just the "correct" solution from that folder. In it, each lists is stored in its own unique way.

Building a sub menu would mean creating some special case to one of them, then alterting the Waitress class to handle it. It'd be a mess.

## Composite Pattern

We turn all the lists into an old-fashion, computer-science tree. Every actual menu item is a leaf, everything else holds a menu.

Waitress becomes much easier. We just pass her the top level menu node.

## OO Principle

