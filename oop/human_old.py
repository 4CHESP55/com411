from inhabitant import Inhabitant

class Robot(Inhabitant):

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name, age):
    super().__init__()
    # An instance attribute
    self.name = name
    self.age = age

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  def grow(self):
    self.age += 1

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, laws={Robot.laws})'
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'

class Human(Inhabitant):

  def __init__(self, name, age):
    super().__init__()
    self.name = name
    self.age = age

  def display(self):
    print(f"I am {self.name}")
  
  def grow(self, amount):
    self.age += amount

  def eat(self, amount):
    if (self.energy + amount) <= Human.MAX_ENERGY:
      self.energy += amount
    else:
      self.energy = Human.MAX_ENERGY
  
  def move(self, distance):
    if (self.energy - distance) >= 0:
      self.energy -= distance
    else:
      print("Can't move, not enough energy!")
  
  def __repr__(self):
    super().__repr__()
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'
  
  def __str__(self):
    super().__str__()
    return f'My name is {self.name}, I am {self.age} years old and have {self.energy} energy.'

if (__name__ == "__main__"):
  human = Human("Paul", 12)
  print(human.__repr__())
  human.move(40)
  print(human.__repr__())
  human.eat(20)
  print(human.__repr__())
  human.eat(100)
  print(human.__repr__())


