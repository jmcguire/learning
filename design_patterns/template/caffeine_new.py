from abc import abstractmethod

# abstract caffeine class

class CaffeinatedBeverage(object):

  def prepare(self):
    self.boil_water()
    self.brew()
    self.pour_in_cup()
    self.add_condiments()

  def boil_water(self):
    print "boiling water"

  @abstractmethod
  def brew(self): pass

  def pour_in_cup(self):
    print "adding sugar and milk"

  @abstractmethod
  def add_condiments(self): pass

# concrete caffeine injection systems

class Coffee(CaffeinatedBeverage):
  def brew(self):
    print "dripping coffee through filter"
  def add_condiments(self):
    print "adding sugar and milk"

class Tea(CaffeinatedBeverage):
  def brew(self):
    print "steeping tea bag"
  def add_condiments(self):
    print "adding a spot of lemon"

# testing

if __name__ == '__main__':

  coffee = Coffee()
  tea = Tea()

  print "making coffee..."
  coffee.prepare()

  print "\nmaking tea..."
  tea.prepare()

