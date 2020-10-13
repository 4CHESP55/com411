def display_ladder(steps):
  print("\n| |\n***"*steps)

def create_ladder():
  print("How many steps remain?")
  display_ladder(int(input()))

def run():
  create_ladder()