class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    self.name = name
    self.age = age
    self.energy = energy
    pass
  
  def __repr__(self):
    return f'Inhabitant(name={self.name}, age={self.age}, energy={self.energy})'
  
  def __str__(self):
    return f'My name is {self.name}, I am {self.age} years old and have {self.energy} energy.'
