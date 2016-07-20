from gumball_monitor_original import GumballMonitor, GumballMachine

# this is a pretty generic wrapper object

class GumballMachineProxy(object):
  """hold a GumballMachine, and call pass on attribute calls"""

  def __init__(self, gumball_machine):
    self.machine = gumball_machine

  def __getattr__(self, attr):
    """call the attribute on our gumball machine"""

    #print "checking for attribute %r remotely" % attr

    # note that this will fail if it doesn't exist, and that's good
    check_attr = getattr(self.machine, attr)

    if callable(check_attr):
      # it's a method, call it and return it
      def wrap_remote_call(*args, **kargs):
        return check_attr(*args, **kargs)
      return wrap_remote_call
    else:
      # it' just an attribute, return it
      return check_attr

if __name__ == '__main__':

  gumball_machine = GumballMachine("Boston", 112)
  proxy = GumballMachineProxy(gumball_machine)
  monitor = GumballMonitor(proxy)

  monitor.report()

