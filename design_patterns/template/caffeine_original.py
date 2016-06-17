
# concrete caffeine injection systems

class Coffee(object):
  def prepare(self):
    self.boil_water()
    self.brew_grinds()
    self.pour_in_cup()
    self.add_sugar_and_milk()
  def boil_water(self):
    print "boiling water"
  def brew_grinds(self):
    print "dripping coffee through filter"
  def pour_in_cup(self):
    print "pouring in cup"
  def add_sugar_and_milk(self):
    print "adding sugar and milk"

class Tea(object):
  def prepare(self):
    self.boil_water()
    self.steep()
    self.pour_in_cup()
    self.add_lemon()
  def boil_water(self):
    print "boiling water"
  def steep(self):
    print "steeping tea bag"
  def pour_in_cup(self):
    print "pouring in cup"
  def add_lemon(self):
    print "adding a spot of lemon"

# testing

coffee = Coffee()
tea = Tea()

print "making coffee..."
coffee.prepare()

print "\nmaking tea..."
tea.prepare()

