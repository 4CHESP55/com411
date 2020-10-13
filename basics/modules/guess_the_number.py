import random
print("Please enter the minimum value:")
minval = int(input())
print("Please enter the maximum value:")
maxval = int(input())
randnum = random.randrange(minval, maxval)
print("I am thinking of a number between {} and {}.  Can you guess what it is?".format(minval,maxval))
guess = int(input())
while guess != randnum:
  if guess > randnum:
    print("Your guess is too high.")
    print("Try again: ")
    guess = int(input())
  elif guess < randnum:
    print("Your guess is too low.")
    print("Try again: ")
    guess = int(input())
print("Congratulations! You guessed my number!")