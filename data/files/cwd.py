def cwd():
  import os
  path = os.getcwd()
  print(f"The current working folder is {path}")
  print("The folder contains the following:")
  for file in os.listdir(path):
    print(file)

def run():
  print("Processing...")
  cwd()

run()