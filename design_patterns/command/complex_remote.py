from abc import abstractmethod

# abstract command class

class Command(object):
  @abstractmethod
  def execute(self): pass
  @abstractmethod
  def undo(self): pass

# special concrete implementations of command, these are helpers for remote

class NoCommand(Command):
  """our null command"""
  def execute(self):
    print "  <<no command>>"
  def undo(self):
    print "  <<no command>>"

class MacroCommand(Command):
  """a group of commands that can be executed all at once"""
  def __init__(self, *commands):
    self.commands = commands
  def execute(self):
    for command in self.commands:
      command.execute()
  def undo(self):
    for command in self.commands:
      command.undo()

# concrete implementations of command, which just wrap our random classes

class Light(object):
  def __init__(self, where):
    self.where = where
  def on(self):
    print "  %s light was turned on" % self.where
  def off(self):
    print "  %s light was turned off" % self.where

class LightOnCommand(Command):
  def __init__(self, light):
    self.light = light
  def execute(self):
    self.light.on()
  def undo(self):
    self.light.off()

class LightOffCommand(Command):
  def __init__(self, light):
    self.light = light
  def execute(self):
    self.light.off()
  def undo(self):
    self.light.off()

class GarageDoor(object):
  def door_up(self):
    print "  garage door went up"
  def door_down(self):
    print "  garage door went down"
  def light_on(self):
    print "  garage light was turned on"
  def light_off(self):
    print "  garage light was turned off"

class GarageDoorOpenCommand(Command):
  def __init__(self, door):
    self.door = door
  def execute(self):
    self.door.door_up()
    self.door.light_on()
  def undo(self):
    self.door.door_down()
    self.door.light_off()

class GarageDoorCloseCommand(Command):
  def __init__(self, door):
    self.door = door
  def execute(self):
    self.door.door_down()
    self.door.light_off()
  def undo(self):
    self.door.door_up()
    self.door.light_on()

class Stereo(object):
  def __init__(self):
    self.volume = 1
  def on(self):
    print "  stereo turned on"
  def off(self):
    print "  stereo turned off"
  def set_volume(self, volume):
    self.volume = volume
    print "  stereo volume turned up to %d" % volume
  def set_cd(self):
    print "  stereo set to CD player"

class StereoCDOnCommand(Command):
  def __init__(self, stereo):
    self.stereo = stereo
    self.previous_volume = None
  def execute(self):
    self.previous_volume = self.stereo.volume

    self.stereo.on()
    self.stereo.set_cd()
    self.stereo.set_volume(11)
  def undo(self):
    # our stereo required a more complicated undo command, for volume
    self.stereo.off()
    self.stereo.set_volume(self.previous_volume)

class StereoCDOffCommand(Command):
  def __init__(self, stereo):
    self.stereo = stereo
    self.previous_volume = None
  def execute(self):
    self.previous_volume = self.stereo.volume

    self.stereo.off()
  def undo(self):
    self.stereo.on()
    self.stereo.set_cd()
    self.stereo.set_volume(self.previous_volume)

# and the remote control that uses the command wrappers

def checkbounds(func):
  def wrapper(self, slot, *args):
    if slot <= 6:
      return func(self, slot, *args)
    else:
      raise Exception("slot number %d is out of bounds" % slot)
  return wrapper

class RemoteControl(object):
  """hold seven commands"""
  def __init__(self):
    """create seven slots and initialize each one"""
    self.on_commands = []
    self.off_commands = []

    no_command = NoCommand()
    self.no_command = no_command
    for _ in range(7):
      self.on_commands.append(no_command)
      self.off_commands.append(no_command)

    self.undo_command = no_command

  @checkbounds
  def set_slot(self, slot, on_command, off_command):
    """set the on and off commands for a particular slot"""
    self.on_commands[slot] = on_command
    self.off_commands[slot] = off_command

  @checkbounds
  def turn_on(self, slot):
    print "slot %d turned on..." % slot
    self.on_commands[slot].execute()
    self.undo_command = self.on_commands[slot]

  @checkbounds
  def turn_off(self, slot):
    print "slot %d turned off..." % slot
    self.off_commands[slot].execute()
    self.undo_command = self.off_commands[slot]

  def undo(self):
    print "undoing last command..."
    self.undo_command.undo()
    self.undo_command = self.no_command

  def display(self):
    print "remote control:"
    for slot in range(7):
      on_class = self.on_commands[slot].__class__.__name__
      off_class = self.off_commands[slot].__class__.__name__
      print "\tslot %d: %s, %s" % (slot + 1, on_class, off_class)

# testing

if __name__ == '__main__':

  def remote_loader(remote):
    kitchen_light = Light("kitchen")
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    bedroom_light = Light("bedroom")
    bedroom_light_on = LightOnCommand(bedroom_light)
    bedroom_light_off = LightOffCommand(bedroom_light)

    garage_door = GarageDoor()
    garage_door_open = GarageDoorOpenCommand(garage_door)
    garage_door_close = GarageDoorCloseCommand(garage_door)

    stereo = Stereo()
    stereo_on = StereoCDOnCommand(stereo)
    stereo_off = StereoCDOffCommand(stereo)

    remote.set_slot(0, kitchen_light_on, kitchen_light_off)
    remote.set_slot(1, bedroom_light_on, bedroom_light_off)
    remote.set_slot(2, garage_door_open, garage_door_close)
    remote.set_slot(3, stereo_on, stereo_off)

    # now lets set up some macros.
    # these macros don't really have a good concept of "off", so we're giving them
    # a null step instead.
    no_command = NoCommand()
    come_home_macro = MacroCommand(garage_door_open, kitchen_light_on, stereo_on)
    head_to_bed_macro = MacroCommand(kitchen_light_off, stereo_off, bedroom_light_on)

    remote.set_slot(5, come_home_macro, no_command)
    remote.set_slot(6, head_to_bed_macro, no_command)

  remote = RemoteControl()
  remote_loader(remote)

  remote.display()
  print

  remote.turn_on(0)
  remote.undo()
  remote.turn_on(1)
  remote.turn_on(2)
  remote.turn_on(3)
  remote.undo()
  print

  remote.turn_off(1)
  remote.turn_off(2)
  remote.undo()
  remote.turn_on(3)
  remote.turn_off(3)
  remote.undo()
  print

  # test macro commands

  print "testing macro commands"

  remote.turn_on(5)
  remote.turn_off(5)

  remote.turn_on(5)
  remote.undo()

