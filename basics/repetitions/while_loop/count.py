def run():
  print("How many live cables must I avoid?")
  num = int(input())
  live = 0

  while live < num:
    print("Avoiding...", end="")
    live = live + 1
    if live > 1:
      s = "s"
    else:
      s = ""
    print("Done! {} live cable{} avoided!".format(live, s))

  print("All live cables have been avoided.")