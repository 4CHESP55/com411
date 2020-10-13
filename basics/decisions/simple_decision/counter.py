def run():
  numEven = 0
  numOdd = 0

  print("Please enter the first whole number.")
  num = int(input())
  if (num % 2 == 0):
      numEven = numEven + 1
  else:
      numOdd = numOdd + 1
  print("Please enter the second whole number.")
  num = int(input())
  if (num % 2 == 0):
      numEven = numEven + 1
  else:
      numOdd = numOdd + 1
  print("Please enter the third whole number.")
  num = int(input())
  if (num % 2 == 0):
      numEven = numEven + 1
  else:
      numOdd = numOdd + 1

  print("There were {} even and {} odd numbers.".format(numEven, numOdd))

