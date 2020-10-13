def sum_weights(w1,w2):
  total = w1+w2
  return total

def calc_avg_weight(w1,w2):
  total = sum_weights(w1,w2)
  average = total/2
  return average

def run():
  print("What is the weight of Beep? ")
  w1 = int(input())
  print("What is the weight of Bop? ")
  w2 = int(input())
  print("What would you like to calculate (sum or average)?")
  calc = input()
  if calc == "sum":
    print("The sum of Beep and Bop's weight is {}.".format(sum_weights(w1,w2)))
  elif calc == "average":
    print("The average of Beep and Bop's weight is {}.".format(calc_avg_weight(w1,w2)))
  else:
    print("incorrect calculation selected!")

run()