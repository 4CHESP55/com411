from tech import Tech

class Laser(Tech):

  MAX_RANGE = 100

  def __init__(self):
    super().__init__()

  def activate(self):
    print("Laser has been activated!")

  def deactivate(self):
    print("Laser has been deactivated!")

  def fire(range_distance):
    if (range_distance > Laser.MAX_RANGE):
      print(f"Fire maximum range of {Laser.MAX_RANGE}")
    else:
      print(f"Fired a distance of {range_distance}.")