import matplotlib.pyplot as plt

def coordinate():
  print("Please enter an x value: ")
  x = int(input())
  print("Please enter a y values: ")
  y = int(input())
  coordinate = (x, y)
  return coordinate

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for x in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  path = (x_values, y_values)
  return path

def run():
  values = path()
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.plot(values[0], values[1], 'ro--')
  plt.show()

run()