from abc import abstractmethod

# core, abstract class

class Beverage(object):
  description = ''
  milk = None
  soy = None
  mocha = None
  whip = None

  def get_description(self):
    print self.description

  def cost(self):
    cost = 0.89
    if self.get_milk():  cost += 0.10
    if self.get_soy():   cost += 0.15
    if self.get_mocha(): cost += 0.20
    if self.get_whip():  cost += 0.10
    return cost

  def get_milk(self):  return self.milk
  def get_soy(self):   return self.soy
  def get_mocha(self): return self.mocha
  def get_whip(self):  return self.whip

  def set_milk(self):  self.milk  = True
  def set_soy(self):   self.soy   = True
  def set_mocha(self): self.mocha = True
  def set_whip(self):  self.whip  = True

# concrete classes

class HouseBlend(Beverage):
  def __init__(self):
    self.description = "Regular House Blend"

class DarkRoast(Beverage):
  def __init__(self):
    self.description = "Most Excellent Dark Roast"
  def cost(self):
    return super(DarkRoast, self).parent_function() + 0.10

class Decaf(Beverage):
  def __init__(self):
    self.description = "Literally Poison"
  def cost(self):
    return super(Decaf, self).parent_function() - 0.16

class Espresso(Beverage):
  def __init__(self):
    self.description = "Quick Hit Espresso"
  def cost(self):
    return super(Espresso, self).parent_function() - 1.10

