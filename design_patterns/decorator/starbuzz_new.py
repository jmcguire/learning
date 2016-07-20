from abc import abstractmethod

# core, abstract class

class Beverage(object):

  def __init__(self): self.description = '<<Unknown Beverage>>'

  def get_description(self): return self.description

  @abstractmethod
  def cost(self): pass

# concrete classes

class HouseBlend(Beverage):
  def __init__(self): self.description = "Regular House Blend"
  def cost(self): return 0.89

class DarkRoast(Beverage):
  def __init__(self): self.description = "Most Excellent Dark Roast"
  def cost(self): return 0.99

class Decaf(Beverage):
  def __init__(self): self.description = "Literally Poison"
  def cost(self): return 1.10

class Espresso(Beverage):
  def __init__(self): self.description = "Quick Hit Espresso"
  def cost(self): return 1.99

# decorator classes

class CondimentDecorator(Beverage):
  pass

class Milk(CondimentDecorator):
  def __init__(self, beverage): self.beverage = beverage
  def cost(self): return self.beverage.cost() + 0.10
  def get_description(self): return self.beverage.get_description() + ", Milk"

class Mocha(CondimentDecorator):
  def __init__(self, beverage): self.beverage = beverage
  def cost(self): return self.beverage.cost() + 0.20
  def get_description(self): return self.beverage.get_description() + ", Mocha"

class Soy(CondimentDecorator):
  def __init__(self, beverage): self.beverage = beverage
  def cost(self): return self.beverage.cost() + 0.15
  def get_description(self): return self.beverage.get_description() + ", Soy"

class Whip(CondimentDecorator):
  def __init__(self, beverage): self.beverage = beverage
  def cost(self): return self.beverage.cost() + 0.10
  def get_description(self): return self.beverage.get_description() + ", Whip"

# testing

if __name__ == '__main__':

  def display(beverage):
    print "%s $%.2f" % (beverage.get_description(), beverage.cost())

  b1 = Espresso()
  display(b1)

  b2 = DarkRoast()
  b2 = Mocha(b2)
  b2 = Mocha(b2)
  b2 = Whip(b2)
  display(b2)

  b3 = HouseBlend()
  b3 = Soy(b3)
  b3 = Mocha(b3)
  b3 = Whip(b3)
  display(b3)

