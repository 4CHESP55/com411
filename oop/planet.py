import human as human

class Planet:
  humans = []
  robots = []

  def __init__(self):
    self.humans = Planet.humans
    self.robots = Planet.robots

  def add_human(self, name, age, move, grow, eat):
    newHuman = human.Human(name, age)
    if move > 0:
      newHuman.move(move)
    if grow > 0:
      newHuman.grow(grow)
    if eat > 0:
      newHuman.eat(eat)
    self.humans.append(newHuman)
  def add_robot(self, name, age):
    newRobot = human.Robot(name, age)
    self.robots.append(newRobot)

  def remove_human(self, num):
    self.humans.pop(num)
  def remove_robot(self, num):
    self.robots.pop(num)

  def __repr__(self):
    return f'Planet(humans={self.humans}, robots={self.robots})'
  
  def __str__(self):
    return f'list of humans {self.humans}, list of robots {self.robots}.'

planet = Planet()
print(planet.__repr__())
planet.add_human("Paul", 23, 0, 0, 0)
planet.add_human("Paul", 23, 50, 3, 23)
planet.add_robot("BEEP", 2)
print(planet.__repr__())
planet.remove_human(0)
print(planet.__repr__())
