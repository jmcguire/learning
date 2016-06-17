from abc import abstractmethod

# our duck classes

class Duck(object):
  """abstract class for ducks"""
  @abstractmethod
  def quack(self): pass
  @abstractmethod
  def fly(self): pass

class MallardDuck(Duck):
  """a type of duck"""
  def quack(self):
    print "*quack*"
  def fly(self):
    print "*flap flap*"

# our incompatible turkey classes

class Turkey(object):
  """abstract class for turkeys"""
  @abstractmethod
  def gobble(self): pass
  @abstractmethod
  def fly(self): pass

class WildTurkey(Turkey):
  """implement a turkey. which is not a duck. not at all"""
  def gobble(self):
    print "*gobble gobble*"
  def fly(self):
    print "*flying a short distance*"

# our adaptor class

class TurkeyAdaptor(Duck):
  def __init__(self, turkey):
    self.turkey = turkey
  def quack(self):
    self.turkey.gobble()
  def fly(self):
    for i in range(3):
      self.turkey.fly()

# testing

def test_duck(duck):
  print "testing out this duck's ability to quack and fly..."
  duck.quack()
  duck.fly()
  print

mallard = MallardDuck()
wild_turkey = WildTurkey()
turkey_in_disguise = TurkeyAdaptor(wild_turkey)

test_duck(mallard)
test_duck(turkey_in_disguise)

