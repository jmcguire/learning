
# home theatre component classes

class PopcornMaker(object):
  def on(self): print "popcorn maker turned on"
  def off(self): print "popcorn maker turned off"
  def pop(self): print "popcorn maker popping"

class Lights(object):
  def dim(self): print "light dimmed"
  def full(self): print "light turned on full bright"

class Screen(object):
  def lower(self): print "screen lowered"
  def raise_(self): print "screen raised"

class DvdPlayer(object):
  def on(self): print "dvd player turned on"
  def off(self): print "dvd player turned off"
  def play(self): print "dvd player playing"

# testing

popcorn = PopcornMaker()
lights = Lights()
screen = Screen()
dvd = DvdPlayer()

print "starting movie..."
popcorn.on()
popcorn.pop()
lights.dim()
screen.lower()
dvd.on()
dvd.play()

print "\ndone with movie..."
dvd.off()
screen.raise_()
lights.full()
popcorn.off()

