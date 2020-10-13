print("Program Started!")
print("Please enter a standard character: ")
char1 = input()
if len(char1) == 1:
  ascii = ord(char1)
  print("The ASCII code for {} is {}.".format(char1, ascii))
else:
  print("input is not a single charater!")

print("Program Ended!")