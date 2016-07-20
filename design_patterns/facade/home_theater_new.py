
# component classes

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

# home theatre facade

class HomeTheatreFacade(object):
  def __init__(self, popcorn, lights, screen, dvd):
    self.popcorn = popcorn
    self.lights = lights
    self.screen = screen
    self.dvd = dvd

  def watch_movie(self):
    self.popcorn.on()
    self.popcorn.pop()
    self.lights.dim()
    self.screen.lower()
    self.dvd.on()
    self.dvd.play()

  def end_movie(self):
    self.dvd.off()
    self.screen.raise_()
    self.lights.full()
    self.popcorn.off()

# testing

if __name__ == '__main__':

  popcorn = PopcornMaker()
  lights = Lights()
  screen = Screen()
  dvd = DvdPlayer()

  home_theatre = HomeTheatreFacade(popcorn, lights, screen, dvd)

  print "starting movie..."
  home_theatre.watch_movie()

  print "\ndone with movie..."
  home_theatre.end_movie()

