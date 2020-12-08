from human import Human
from robot import Robot

class Planet:

  def __init__(self):
    self.inhabitants = []
      
  def countInhabitants(self):
    self.num_humans = 0
    self.num_robots = 0
    for inhabitant in planet.inhabitants:
      if isinstance(inhabitant, Human):
        self.num_humans += 1
      if isinstance(inhabitant, Robot):
        self.num_robots += 1

  def __repr__(self):
    return f"planet(inhabitants={self.inhabitants})"

  def __str__(self):
    Planet.countInhabitants(self)
    return f"This planet has {self.num_humans} humans and {self.num_robots} robots."

  def add_inhabitant(self, inhabitant):
    self.inhabitants.append(inhabitant)

  def remove_inhabitant(self, inhabitant):
    self.inhabitants.remove(inhabitant)

if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  paul = Human("Paul", 12)
  dan = Human("Dan", 32)
  beep = Robot("Beep", 2)
  planet.add_inhabitant(paul)
  planet.add_inhabitant(dan)
  planet.add_inhabitant(beep)
  print(repr(planet))
  print(planet)
  planet.remove_inhabitant(paul)
  print(planet)
  num_humans = 0
  num_robots = 0