def cross_bridge(distance):
  i = 0
  while i < distance:
    print("Crossed step.")
    i = i + 1
  if distance > 5:
    print("The bridge is collapsing!")
  else:
    print("we must keep going!")

def run():
cross_bridge(3)
cross_bridge(6)