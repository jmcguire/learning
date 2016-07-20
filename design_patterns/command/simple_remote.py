from abc import abstractmethod

# abstract command class

class Command(object):
  @abstractmethod
  def execute(self): pass

# concrete implementations of command, which just wrap simpler classes

class LightOnCommand(Command):
  def __init__(self, light):
    self.light = light
  def execute(self):
    self.light.on()

class Light(object):
  def on(self):
    print "light was turned on"

class GarageDoorOpenCommand(Command):
  def __init__(self, door):
    self.door = door
  def execute(self):
    self.door.door_up()
    self.door.light_on()

class GarageDoor(object):
  def door_up(self):
    print "garage door went up"
  def light_on(self):
    print "garage light was turned on"

# and the remote control that uses the command wrappers

class SimpleRemoteControl(object):
  """a simple remote that holds a single command"""
  def set_command(self, command):
    self.slot = command
  def press_button(self):
    self.slot.execute()

# testing

if __name__ == '__main__':

  light_switch = Light()
  light_button = LightOnCommand(light_switch)
  remote = SimpleRemoteControl()
  remote.set_command(light_button)
  remote.press_button()

  garage_door = GarageDoor()
  garage_button = GarageDoorOpenCommand(garage_door)
  remote2 = SimpleRemoteControl()
  remote2.set_command(garage_button)
  remote2.press_button()

