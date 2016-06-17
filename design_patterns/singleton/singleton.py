# create a singleton decorator

def singleton(object_in):
  """decorate a class with this to turn it into a singleton"""
  instances = {}
  def wrapper(*args, **kargs):
    if object_in not in instances:
      instances[object_in] = object_in(*args, **kargs)
      print "created new object"
    else:
      print "using existing object"
    return instances[object_in]
  return wrapper

# potential bug: since this returns a function and not an object, you can't
# directly call on class attributes

# sample object

@singleton
class GlobalCount(object):
  def __init__(self, count):
    self.count = count
  def get_count(self):
    print self.count

# testing

temp_a = GlobalCount(1)
temp_a.get_count()

temp_b = GlobalCount(2)
temp_b.get_count()

temp_a.get_count()

