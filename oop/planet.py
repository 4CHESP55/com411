import human as human

class Planet:
  inhabitants = {
  'humans': [],
  'robots': []
  }

  def __init__(self):
    self.humans = Planet.inhabitants['humans']
    self.robots = Planet.inhabitants['robots']

  def add_human(self, name, age):
    newHuman = human.Human(name, age)
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
planet.add_human("Paul", 23)
planet.add_human("Paul", 26)
planet.add_robot("BEEP", 2)
print(planet.__repr__())
planet.remove_human(0)
print(planet.__repr__())
print(Planet.inhabitants)
