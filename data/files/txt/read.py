def search(file_name):
  print("Searching...")
  with open(file_name) as file:
    for line in file:
      print(f"Looked in {line}.", end="")
  print('\n'"...Done!")

def run():
  search("locations.txt")

run()