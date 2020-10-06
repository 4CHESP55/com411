print("What type of adventure should I have?")
adType = input()
if (adType == "scary") or (adType == "short"):
  print("Entering the dark forest!")
elif (adType == "safe") or (adType == "long"):
  print("Taking the safe route!")
else:
  print("Not sure which route to take")