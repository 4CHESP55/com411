import csv
import matplotlib.pyplot as plt

def read_data():
  line = []
  data = {}
  with open("temps.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
      line.append(row)
  for column in range(len(line[0])):
    rows = []
    for row in range(1, len(line)):
      rows.append(float(line[row][column]))
    data[line[0][column]] = rows
  return data

def run():
  data = read_data()
  values_list = list(data)
  keys_list = list(data.keys())
  fig, axs = plt.subplots(1, len(data))
  for x in range(len(data)):
    axs[x].set_title(keys_list[x])
    axs[x].set_xlabel('Record')
    axs[x].set_ylabel('Temperature')
    axs[x].plot(list(range(1, len(data[values_list[x]])+1)), data[values_list[x]])

  plt.show()

run()
