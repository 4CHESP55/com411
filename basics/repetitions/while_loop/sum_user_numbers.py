def run():
  print("How many numbers should I sum up?")
  num = int(input())
  i = 0
  total = 0
  while i < num:
    i = i + 1
    print("Please enter number {} of {}.".format(i,num))
    inNum = int(input())
    total = total + inNum
  print("The answer is {}.".format(total))