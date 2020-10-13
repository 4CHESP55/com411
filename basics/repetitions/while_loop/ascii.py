def run():
  print("How many bars should be charged?")
  bars = int(input())
  charged = 0
  while charged < bars:
    charged = charged + 1
    print("Charging: ","█ "*charged)

  print("The battery is fully charged.")