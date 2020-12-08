from clothing_size import ClothingSize

class Clothing:
  def __init__(self, colour, material, size):
    self.colour = colour
    self.material = material
    self.size = size

  def check_size(self, clothing):
    if (clothing == ClothingSize.MEDIUM):
      print("Medium!")

if __name__ == "__main__":
  red_silk = Clothing("Red", "Silk", ClothingSize.MEDIUM)
  print(ClothingSize(3))
  red_silk.check_size(2)