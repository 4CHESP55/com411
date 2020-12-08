from inhabitant import Inhabitant

class Human(Inhabitant):

  # initialiser
  def __init__(self, name="Human", age=0):
    super().__init__(name, age)

  # magic methods
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  human.grow()
  print(repr(human))
  human.eat(20)
  print(repr(human))