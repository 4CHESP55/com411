print("Towards which direction should I paint (up, down, left or right)?")
direction = input()

if (direction == "up"):
  print("I am painting in the upward direction!")
elif (direction == "down"):
  print("I am painting in the downwards direction!")
elif (direction == "left"):
  print("I am painting in the left direction!")
elif (direction == "right"):
  print("I am painting in the right direction!")
else:
  print("I do not recognise the direction {}".format(direction))
