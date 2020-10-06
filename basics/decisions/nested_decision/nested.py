print("What type of cover does the book have?")
booktype = input()
if (booktype == "soft"):
  print("Is the book perfect bound?")
  bound = input()
  if (bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")
elif (booktype == "hard"):
  print("Books with hard covers can be more expensive!")
else:
  print("I do not recognise the cover type of {}.".format(booktype))