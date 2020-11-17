import csv
import matplotlib.pyplot as plt

def isFloat(string):
  try:
    float(string)
    return True
  except ValueError:
    return False

def read_data():
  line = []
  data = {}
  with open("titanic.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
      line.append(row)
  for column in range(len(line[0])):
    rows = []
    for row in range(1, len(line)):
      float_pos = isFloat(line[row][column])
      if float_pos == True:
        rows.append(round(float(line[row][column]),2))
      else:
        rows.append(line[row][column])
    data[line[0][column]] = rows
  return (data)

def run():
  data = read_data()
  fig, axs = plt.subplots(2, 2)
  sex = [list(data["Sex"]).count("male"), list(data["Sex"]).count("female")]
  axs[0,0].set_xlabel('Sex')
  axs[0,0].set_ylabel('Number')
  axs[0,0].bar(["male", "female"], sex)
  survived = 0
  died = 0
  for entry in range(len(list(data["Survived"]))):
    if list(data["Survived"])[entry] == 1.0:
      survived = survived + 1
    else:
      died = died + 1
  axs[0,1].set_xlabel('Status')
  axs[0,1].set_ylabel('Number')
  axs[0,1].bar(["Survived", "Died"], [survived, died])
  
  axs[1,1].set_xlabel('Age')
  axs[1,1].set_ylabel('Fare')
  axs[1,1].scatter(list(data["Age"]), list(data["Fare"]))
  print(list(data["Age"]))
    

  plt.show()

run()