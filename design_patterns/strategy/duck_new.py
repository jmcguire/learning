from abc import abstractmethod

# flying behaviors

class FlyBehavior(object):
  @abstractmethod
  def fly(self): pass

class FlyWithWings(FlyBehavior):
  def fly(self): print "*flap flap*"

class FlyNoWay(FlyBehavior):
  def fly(self): print "<< i cannot fly >>"

class FlyRocketPowered(FlyBehavior):
  def fly(self): print "*rocketed*"

# quacking behaviors

class QuackBehavior(object):
  @abstractmethod
  def quack(self): pass

class Quack(QuackBehavior):
  def quack(self): print "*quack*"

class Squeak(QuackBehavior):
  def quack(self): print "*squeak*"

class MuteQuack(QuackBehavior):
  def quack(self): print "<< silence >>*"

# core, abstract class

class Duck(object):
  def __init__(self):
    self.fly_behevior = None
    self.quack_behevior = None

  def perform_quack(self): self.quack_behavior.quack()
  def perform_fly(self): self.fly_behavior.fly()
  def swim(self): print "*swimming*"
  def set_fly_behavior(self, fb): self.fly_behavior = fb
  def set_quack_behavior(self, qb): self.quack_behavior = qb

  @abstractmethod
  def display(self): pass

# concrete classes

class Mallard(Duck):
  def __init__(self):
    self.fly_behavior = FlyWithWings()
    self.quack_behavior = Quack()
    super(Mallard, self).__init__()
  def display(self): print "i'm a mallard"

class RedHeadDuck(Duck):
  def __init__(self):
    self.fly_behavior = FlyWithWings()
    self.quack_behavior = Quack()
    super(RedHeadDuck, self).__init__()
  def display(self): print "i'm a red headed duck"

class RubberDuck(Duck):
  def __init__(self):
    self.fly_behavior = FlyNoWay()
    self.quack_behavior = Squeak()
    super(RubberDuck, self).__init__()
  def display(self): print "i'm a rubber duck"

class DecoyDuck(Duck):
  def __init__(self):
    self.fly_behavior = FlyNoWay()
    self.quack_behavior = MuteQuack()
    super(DecoyDuck, self).__init__()
  def display(self): print "i'm a wooden decoy duck"

class ModelDuck(Duck):
  def __init__(self):
    self.fly_behavior = FlyNoWay()
    self.quack_behavior = Quack()
    super(ModelDuck, self).__init__()
  def display(self): print "i'm a model duck"

# testing

if __name__ == '__main__':

  for duck in Mallard(), RedHeadDuck(), RubberDuck(), DecoyDuck():
    duck.display()
    duck.perform_quack()
    duck.swim()
    duck.perform_fly()
    print ""

  duck = ModelDuck()
  duck.display()
  duck.perform_fly()
  duck.set_fly_behavior(FlyRocketPowered())
  duck.perform_fly()
  print ""

