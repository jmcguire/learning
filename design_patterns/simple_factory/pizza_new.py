
# dumb pizza classes

class Pizza(object):
  def prepare(self): pass
  def bake(self): pass
  def cut(self): pass
  def box(self): pass

class CheesePizza(Pizza): pass
class GreekPizza(Pizza): pass
class PepperoniPizza(Pizza): pass
class ClamPizza(Pizza): pass
class VeggiePizza(Pizza): pass

# factory class

class PizzaFactory(object):
  """ figure out what type of pizza to make """

  def create_pizza(self, pizza_type):
    pizza = object

    if pizza_type == 'cheese':
      pizza = CheesePizza()
    elif pizza_type == 'greek':
      pizza = GreekPizza()
    elif pizza_type == 'pepperoni':
      pizza = PepperoniPizza()
    elif pizza_type == 'clam':
      pizza = ClamPizza()
    elif pizza_type == 'veggie':
      pizza = VeggiePizza()

    return pizza

# store class

class PizzaStore(object):

  def __init__(self, factory):
    self.factory = factory

  def order_pizza(self, pizza_type):
    pizza = self.factory.create_pizza()

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()

    return pizza


# testing

if __name__ == '__main__':

  factory = PizzaFactory()
  store = PizzaStore(factory)

