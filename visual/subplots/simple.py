import matplotlib.pyplot as plt

def read_data(file_name):
  temps = []
  with open(file_name) as file:
    for line in file:
      temps.append(float(line.replace('\n', '')))
  return temps

def run():
  data = read_data('temps.txt')
  num = list(range(1, len(data)+1))
  print(num)
  fig, axs = plt.subplots(1, 2)
  axs[0].set_xlabel('Record')
  axs[0].set_ylabel('Temperature')
  axs[0].plot(num, data)
  
  axs[1].set_xlabel('Record')
  axs[1].set_ylabel('Temperature')
  axs[1].bar(num, data)
  plt.show()

run()