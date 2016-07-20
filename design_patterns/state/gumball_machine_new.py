from random import randint

# state classes

class State(object):
  def insert_quarter(self): pass
  def eject_quarter(self): pass
  def turn_crank(self): pass
  def dispence(self): pass

class SoldState(State):
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
  def insert_quarter(self):
    print "Please wait, we're already giving you a gumball"
  def eject_quarter(self):
    print "Sorry, you already turned the crank"
  def turn_crank(self):
    print "Turning the crank twice doesn't give you another gumball"
  def dispence(self):
    self.gumball_machine.release_gumball()
    if self.gumball_machine.count == 0:
      print "Oops, we are now out of gumballs"
      self.gumball_machine.state = self.gumball_machine.sold_out_state
    else:
      self.gumball_machine.state = self.gumball_machine.no_quarter_state

class SoldOutState(State):
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
  def insert_quarter(self):
    print "Can't insert a quarter, machine is sold out"
  def eject_quarter(self):
    print "You can't eject, you haven't inserted a quarter yet"
  def turn_crank(self):
    print "You turned the crank, but there are no gumballs"
  def dispence(self):
    print "No gumball dispenced"

class NoQuarterState(State):
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
  def insert_quarter(self):
    print "You inserted a quarter"
    self.gumball_machine.state = self.gumball_machine.has_quarter_state
  def eject_quarter(self):
    print "You haven't inserted a quarter"
  def turn_crank(self):
    print "You turned the crank, but there's no quarter"
  def dispence(self):
    print "You need to pay first"

class HasQuarterState(State):
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
  def insert_quarter(self):
    print "Can't insert another quarter"
  def eject_quarter(self):
    print "Quarter returned"
    self.gumball_machine.state = self.gumball_machine.no_quarter_state
  def turn_crank(self):
    print "You turned..."
    if randint(1, 10) == 10:
      self.gumball_machine.state = self.gumball_machine.winner_state
    else:
      self.gumball_machine.state = self.gumball_machine.sold_state
  def dispence(self):
    print "No gumball dispenced"

class WinnerState(State):
  def __init__(self, gumball_machine):
    self.gumball_machine = gumball_machine
  def insert_quarter(self):
    print "Currently winning, no need for another quarter yet"
  def eject_quarter(self):
    print "Currently winning, can't get your quarter back now"
  def turn_crank(self):
    print "You already turned the crank"
  def dispence(self):
    print "You're a winner!"
    self.gumball_machine.release_gumball()
    if self.gumball_machine.count == 0:
      print "Oops, we are now out of gumballs"
      self.gumball_machine.state = self.gumball_machine.sold_out_state
    else:
      self.gumball_machine.release_gumball()
      if self.gumball_machine.count == 0:
        print "Oops, we are now out of gumballs"
        self.gumball_machine.state = self.gumball_machine.sold_out_state
      else:
        self.gumball_machine.state = self.gumball_machine.no_quarter_state


# base class

class GumballMachine(object):
  def __init__(self, count):
    self.count = count

    self.sold_out_state = SoldOutState(self)
    self.sold_state = SoldState(self)
    self.no_quarter_state = NoQuarterState(self)
    self.has_quarter_state = HasQuarterState(self)
    self.winner_state = WinnerState(self)

    self.state = self.sold_out_state
    if count > 0:
      self.state = self.no_quarter_state

  def show_state(self):
    print "\nMighty Gumball Machine"
    print "Inventory: %d gumballs" % self.count
    if self.state == self.sold_out_state:
      print "State: sold out"
    elif self.state == self.no_quarter_state:
      print "State: no quarter"
    elif self.state == self.has_quarter_state:
      print "State: has quarter"
    elif self.state == self.sold_state:
      print "State: sold"
    elif self.state == self.winner_state:
      print "State: winner"
    print

  def insert_quarter(self):
    self.state.insert_quarter()

  def eject_quarter(self):
    self.state.eject_quarter()

  def turn_crank(self):
    self.state.turn_crank()
    self.state.dispence()

  def release_gumball(self):
    print "A gumball comes rolling out the slot"
    self.count -= 1


# testing

if __name__ == '__main__':

  gm = GumballMachine(5)
  gm.show_state()

  gm.insert_quarter()
  gm.turn_crank()

  gm.show_state()

  gm.insert_quarter()
  gm.eject_quarter()
  gm.turn_crank()

  gm.show_state()

  gm.insert_quarter()
  gm.turn_crank()
  gm.insert_quarter()
  gm.turn_crank()
  gm.eject_quarter()

  gm.show_state()

  gm.insert_quarter()
  gm.insert_quarter()
  gm.turn_crank()
  gm.insert_quarter()
  gm.turn_crank()
  gm.insert_quarter()
  gm.turn_crank()

  gm.show_state()

