def run():
  print("Please enter a number")
  num = int(input())
  fact = 1
  i = 0
  while i < num:
    i = i + 1
    fact = fact * i

  print("The factorial of {} is {}.".format(num, fact))