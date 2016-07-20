import unittest
from unnecessary_math import multiply

class TestDesignPattern(unittest.TestCase):
  def setUp(self):
    self.mallard = MallardDuck()
    self.wild_turkey = WildTurkey()
    self.turkey_in_disguise = TurkeyAdaptor(wild_turkey)

  def test_mallard(self):
    self.mallard.quack()
    self.mallard.fly()

    self.assertEqual( multiply(3,4), 12)

  def test_disguised_turkey(self):
    self.turkey_in_disguise.quack()
    self.turkey_in_disguise.fly()

    self.assertEqual( multiply('a',3), 'aaa')

if __name__ == '__main__':
  unittest.main()

