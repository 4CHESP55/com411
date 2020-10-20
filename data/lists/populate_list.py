def directions():
  directions = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right" ]
  return directions

def menu():
  print("Please select a direction:")
  move = directions()
  for index in range (len(move)):
    print("{}: {}".format(index, move[index]))
  option = int(input())
  return move[option]

def run():
  route = []
  print("Working out escape route...")
  for count in range (5):
    route.append(menu())
  print("Escape route: {}".format(route))

run()