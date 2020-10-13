def box(word):
  print(" "+"_"*(len(word)+2)+" ")
  print("|"+" "*(len(word)+2)+"|")
  print("| "+word+" |")
  print("|"+"_"*(len(word)+2)+"|")

def lower_case(word):
  print(word.lower())

def upper_case(word):
  print(word.upper())

def mirrored(word):
  for position in range(len(word) - 1, -1, -1):
    print(word[position], end="")

def repeat(word):
  print("How many times to repeat?")
  num = int(input())
  i = 0 
  while i < num:
    if i%2 == 0:
      lower_case(word)
    else:
      upper_case(word)
    i = i + 1

def run():
  print("Please enter a word: ")
  word = input()
  print('''
  Please select an option:
  1) Display in a box
  2) Display Lower-case
  3) Display Upper-case
  4) Display Mirrored
  5) Repeat
  ''')
  option = int(input())
  if option == 1:
    box(word)
  elif option == 2:
    lower_case(word)
  elif option == 3:
    upper_case(word)
  elif option == 4:
    mirrored(word)
  elif option == 5:
    repeat(word)
  else:
    print("invalid option!")

run()