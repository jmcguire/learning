from abc import ABCMeta, abstractmethod

# core, abstract class

class Duck(object):
  def quack(self): print "*quack*"
  def swim(self): print "*swimming*" 
  def fly(self): print "*flap flap*"

  @abstractmethod
  def display(self): pass

# concrete classes

class Mallard(Duck):
  def display(self): print "i'm a mallard"

class RedHeadDuck(Duck):
  def display(self): print "i'm a red headed duck"

class RubberDuck(Duck):
  def display(self): print "i'm a rubber duck"
  def quack(self): print "*squeek*"
  def fly(self): print "<< cannot fly >>"

class DecoyDuck(Duck):
  def display(self): print "i'm a wodden decoy duck"
  def quack(self): print "<< silence >>"
  def fly(self): print "<< cannot fly >>"

# testing

if __name__ == '__main__':

  for duck in Mallard(), RedHeadDuck(), RubberDuck(), DecoyDuck():
    duck.display()
    duck.quack()
    duck.swim()
    duck.fly()
    print ""

