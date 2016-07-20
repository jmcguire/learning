# core, abstract class

class Beverage(object):
  def __init__(self):
    self.milk = False
    self.soy = False
    self.mocha = False
    self.whip = False
    self.description = ''

  def get_description(self):
    return self.description

  def cost(self):
    cost = 0.89
    if self.get_milk(): cost += 0.10
    if self.get_soy(): cost += 0.15
    if self.get_mocha(): cost += 0.20
    if self.get_whip(): cost += 0.10
    return cost

  def get_milk(self): return self.milk
  def get_soy(self): return self.soy
  def get_mocha(self): return self.mocha
  def get_whip(self): return self.whip

  def set_milk(self): self.milk = True
  def set_soy(self): self.soy = True
  def set_mocha(self): self.mocha = True
  def set_whip(self): self.whip = True


# concrete classes

class HouseBlend(Beverage):
  def __init__(self):
    self.description = "Regular House Blend"
    super(HouseBlend, self).__init__()

class DarkRoast(Beverage):
  def __init__(self):
    self.description = "Most Excellent Dark Roast"
    super(DarkRoast, self).__init__()
  def cost(self):
    return super(DarkRoast, self).cost() + 0.10

class Decaf(Beverage):
  def __init__(self):
    self.description = "Literally Poison"
    super(Decaf, self).__init__()
  def cost(self):
    return super(Decaf, self).cost() + 0.16

class Espresso(Beverage):
  def __init__(self):
    self.description = "Quick Hit Espresso"
    super(Espresso, self).__init__()
  def cost(self):
    return super(Espresso, self).cost() + 1.1


# testing

if __name__ == '__main__':

  def display(beverage):
    print "%s $%.2f" % (beverage.get_description(), beverage.cost())

  b1 = Espresso()
  display(b1)

  b2 = DarkRoast()
  b2.set_mocha()
  b2.set_whip()
  display(b2)

  b3 = HouseBlend()
  b3.set_soy()
  b3.set_mocha()
  b3.set_whip()
  display(b3)

