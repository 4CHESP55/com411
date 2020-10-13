print("Program Started!")
print("Please enter an ASCII code: ")
ascii1 = abs(int(input()))
if ascii1 in range(32,126):
  char1 = chr(ascii1)
  print("The character represented by the ASCII code {} is {}.".format(ascii1,char1))
else:
  print("Code is not ascii!")

print("Program Ended!")