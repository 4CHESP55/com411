def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  move = movements()
  x = 0
  y = 1
  for count in range (int(len(move)/2)):
    print("{} for {} steps".format(move[x], move[y]))
    x = x + 2
    y = y + 2

run()

