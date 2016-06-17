
# dumb pizza classes

class Pizza(object):
  def prepare(self): pass
  def bake(self): pass
  def cut(self): pass
  def box(self): pass

class NYCheesePizza(Pizza): pass
class NYGreekPizza(Pizza): pass
class NYPepperoniPizza(Pizza): pass
class NYClamPizza(Pizza): pass
class NYVeggiePizza(Pizza): pass

class ChicagoCheesePizza(Pizza): pass
class ChicagoGreekPizza(Pizza): pass
class ChicagoPepperoniPizza(Pizza): pass
class ChicagoClamPizza(Pizza): pass
class ChicagoVeggiePizza(Pizza): pass

# factory class

class PizzaFactory(object):
  """ an abstract factory """
  def create_pizza(self, pizza_type): pass

class NYPizzaFactory(object):
  """ figure out what type of NY pizza to make """

  def create_pizza(self, pizza_type):
    pizza = object

    if pizza_type == 'cheese':
      pizza = NYCheesePizza()
    elif pizza_type == 'greek':
      pizza = NYGreekPizza()
    elif pizza_type == 'pepperoni':
      pizza = NYPepperoniPizza()
    elif pizza_type == 'clam':
      pizza = NYClamPizza()
    elif pizza_type == 'veggie':
      pizza = NYVeggiePizza()

    return pizza

class ChicagoPizzaFactory(object):
  """ figure out what type of chicago pizza to make """

  def create_pizza(self, pizza_type):
    pizza = object

    if pizza_type == 'cheese':
      pizza = ChicagoCheesePizza()
    elif pizza_type == 'greek':
      pizza = ChicagoGreekPizza()
    elif pizza_type == 'pepperoni':
      pizza = ChicagoPepperoniPizza()
    elif pizza_type == 'clam':
      pizza = ChicagoClamPizza()
    elif pizza_type == 'veggie':
      pizza = ChicagoVeggiePizza()

    return pizza

# store class

class PizzaStore(object):

  def __init__(self, factory):
    self.factory = factory

  def order_pizza(self, pizza_type):
    pizza = self.factory.create_pizza(pizza_type)

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()

    return pizza

# sample code

ny_factory = NYPizzaFactory()
ny_store = PizzaStore(ny_factory)
ny_store.order_pizza('veggie')

chicago_factory = ChicagoPizzaFactory()
chicago_store = PizzaStore(chicago_factory)
chicago_store.order_pizza('veggie')

