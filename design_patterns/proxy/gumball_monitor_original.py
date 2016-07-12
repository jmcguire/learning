
# we don't need the full gumball machine from the "state" design pattern.
# here's a neutered one.

class MachineState:
  sold_out = 0
  no_quarter = 1
  has_quarter = 2
  sold = 3

class GumballMachine(object):
  def __init__(self, location, inventory):
    self.location = location
    self.inventory = inventory
    self.state = MachineState.no_quarter

  def get_state(self):
  	if self.state == MachineState.sold_out:
  		return "sold out"
  	elif self.state == MachineState.no_quarter:
  		return "waiting for quarter"
  	elif self.state == MachineState.has_quarter:
  		return "has quarter"
  	elif self.state == MachineState.sold:
  		return "sold"

# the main class of this exercise

class GumballMonitor(object):
  def __init__(self, machine):
    self.machine = machine
  def report(self):
    print "Gumball Machine: %s" % self.machine.location
    print "Current inventory: %d gumballs" % self.machine.inventory
    print "Current state: %s" % self.machine.get_state()

# testing

if __name__ == '__main__':
  gumball_machine = GumballMachine("Boston", 112)
  monitor = GumballMonitor(gumball_machine)

  monitor.report()

