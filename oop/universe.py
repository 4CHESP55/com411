import planet as planet

class Universe:
  def __init__(self):
    self.planets = []

  def generate(self):
    newPlanet = planet.Planet()
    newPlanet.add_human("Paul", 23)
    newPlanet.add_human("Paul", 26)
    self.planets.append(newPlanet)

universe = Universe()
universe.generate()
universe.generate()
universe.generate()
print(universe.planets)