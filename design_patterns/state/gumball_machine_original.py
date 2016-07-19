
# basic enum

class MachineState:
  sold_out = 0
  no_quarter = 1
  has_quarter = 2
  sold = 3

# base class

class GumballMachine(object):
  def __init__(self, count):
  	self.state = MachineState.sold_out
  	self.count = count
  	if count > 0:
  		self.state = MachineState.no_quarter

  def show_state(self):
  	print "\nMighty Gumball Machine"
  	print "Inventory: %d gumballs" % self.count
  	if self.state == MachineState.sold_out:
  		print "State: sold out"
  	elif self.state == MachineState.no_quarter:
  		print "State: no quarter"
  	elif self.state == MachineState.has_quarter:
  		print "State: has quarter"
  	elif self.state == MachineState.sold:
  		print "State: sold"
  	print

  def insert_quarter(self):
  	if self.state == MachineState.sold_out:
  		print "Can't insert a quarter, machine is sold out"
  	elif self.state == MachineState.no_quarter:
  		print "You inserted a quarter"
  		self.state = MachineState.has_quarter
  	elif self.state == MachineState.has_quarter:
  		print "Can't insert another quarter"
  	elif self.state == MachineState.sold:
  		print "Please wait, we're already giving you a gumball"

  def eject_quarter(self):
  	if self.state == MachineState.sold_out:
  		print "You can't eject, you haven't inserted a quarter yet"
  	elif self.state == MachineState.no_quarter:
  		print "You haven't inserted a quarter"
  	elif self.state == MachineState.has_quarter:
  		print "Quarter returned"
  		self.state = MachineState.no_quarter
  	elif self.state == MachineState.sold:
  		print "Sorry, you already turned the crank"

  def turn_crank(self):
  	if self.state == MachineState.sold_out:
  		print "You turned the crank, but there are no gumballs"
  	elif self.state == MachineState.no_quarter:
  		print "You turned the crank, but there's no quarter"
  	elif self.state == MachineState.has_quarter:
  		print "You turned..."
  		self.state = MachineState.sold
  		self.dispence()
  	elif self.state == MachineState.sold:
  		print "Turning the crank twice doesn't give you another gumball"

  def dispence(self):
  	if self.state == MachineState.sold_out:
  		print "No gumball dispenced"
  	elif self.state == MachineState.no_quarter:
  		print "You need to pay first"
  	elif self.state == MachineState.has_quarter:
  		print "No gumball dispenced"
  	elif self.state == MachineState.sold:
  		print "A gumball comes rolling out the slot"
  		self.count -= 1
  		if self.count == 0:
  			print "Oops, we are now out of gumballs"
  			self.state = MachineState.sold_out
  		else:
  			self.state = MachineState.no_quarter

# testing

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

