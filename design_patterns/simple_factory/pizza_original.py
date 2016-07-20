
# store class

class PizzaStore(object):

  def order_pizza(self, pizza_type):
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

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza

