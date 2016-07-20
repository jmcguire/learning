from abc import abstractmethod

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

# abstract factory store class

class PizzaStore(object):
  """an abstract factory"""

  def order_pizza(self, pizza_type):
    pizza = self.create_pizza(pizza_type)

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()

    return pizza

  @abstractmethod
  def create_pizza(self, pizza_type):
    pass

# store implementations

class NYPizzaStore(PizzaStore):
  """implements an abstract factory be deciding what kind of pizza gets made"""
  def create_pizza(self, pizza_type):
    pizza = None

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

class ChicagoPizzaStore(PizzaStore):
  """implements an abstract factory be deciding what kind of pizza gets made"""
  def create_pizza(self, pizza_type):
    pizza = None

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

# testing

if __name__ == '__main__':

  ny_store = NYPizzaStore()
  ny_store.order_pizza('veggie')

  chicago_store = ChicagoPizzaStore()
  chicago_store.order_pizza('veggie')

