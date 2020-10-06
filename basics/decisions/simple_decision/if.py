print("What type of book is this?")
genre = input()

if (genre == "adventure"):
  print("I like adventure books!")
else:
  print("I don't like {} books!".format(genre))

print("Finished reading book.")