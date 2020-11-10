import matplotlib.pyplot as plt

def data1():
  paths = {}
  print("What type of line do you want? ")
  line_type = input()
  print("what colour would you like?")
  colour = input()
  print("what style marker would you like?")
  marker = input()
  paths['line type'] = line_type
  paths['colour'] = colour
  paths['marker style'] = marker
  return paths

def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  for x in range(num_lines):
    data = data1()
    if data['line type'] == "dotted":
      line_type = ":"
    elif data['line type'] == "dashed":
      line_type = "--"
    elif data['line type'] == "solid":
      line_type = "-"
    else:
      line_type = ""
    if data['colour'] == "red":
      colour = "r"
    elif data['colour'] == "green":
      colour = "g"
    elif data['colour'] == "blue":
      colour = "b"
    else:
      colour = ""
    if data['marker style'] == "circle":
      marker = "o"
    elif data['marker style'] == "square":
      marker = "s"
    elif data['marker style'] == "triangle":
      marker = "^"
    else: 
      marker = ""
    display = f"{marker}{colour}{line_type}"
    x_value = [1, 5]
    y_value = [x, x]
    plt.plot(x_value, y_value, display)

def run():
  print("Running...")
  generate()
  print("...Done!")
  plt.show()

run()
