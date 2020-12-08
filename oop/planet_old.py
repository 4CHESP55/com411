import human as human

class Planet:
  inhabitants = []

  def __init__(self):
    self.inhabitants = Planet.inhabitants
    self.num_humans = 0
    self.num_robots = 0

  def add_human(self, name, age):
    newHuman = human.Human(name, age)
    self.inhabitants.append(newHuman)
  def add_robot(self, name, age):
    newRobot = human.Robot(name, age)
    self.inhabitants.append(newRobot)

  def remove_human(self, num):
    self.inhabitants.pop(num)
  def remove_robot(self, num):
    self.inhabitants.pop(num)

  def count_inhabitants(self):
    num_humans = 0
    num_robots = 0
    for inhabitant in self.inhabitants:
      if isinstance(inhabitant, human.Human):
        num_humans += 1
      if isinstance(inhabitant, human.Robot):
        num_robots += 1
    self.num_humans = num_humans
    self.num_robots = num_robots

  def __repr__(self):
    return f'Planet(humans={self.num_humans}, robots={self.num_robots})'
  
  def __str__(self):
    return f'list of humans {self.num_humans}, list of robots {self.num_robots}.'

if (__name__ == "__main__"):
  planet = Planet()
  planet.count_inhabitants()
  print(planet.__repr__())
  planet.add_human("Paul", 23)
  planet.add_human("Paul", 26)
  planet.add_human("Paul", 26)
  planet.add_robot("BEEP", 2)
  planet.add_robot("BEEP", 4)
  planet.count_inhabitants()
  print(planet.__repr__())
  planet.remove_human(0)
  planet.count_inhabitants()
  print(planet.__repr__())
  print(Planet.inhabitants)
