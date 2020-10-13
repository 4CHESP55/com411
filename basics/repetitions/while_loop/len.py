def run():
  print("Please enter a phrase:")
  phrase = input()
  i = 0
  while i < len(phrase):
    if i == (len(phrase) - 1):
      print("Bop")
    else:
      print("Bop ", end="")
    i = i + 1