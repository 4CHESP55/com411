def search(file_name):
  print("Searching...")
  sections = []
  books = []
  with open(file_name) as file:
    for line in file:
      if line.startswith("Section"):
        section_split = line.split(":")
        sections.append(section_split[1])
      else:
        books.append(line)
  print('\n'"...Done!")
  file_tuple = (sections, books)
  print(file_tuple)
  return file_tuple

def save(file_name, store_tuple):
  print("Saving...")
  with open(file_name, "w") as file:
    file.write("Sections:\n")
    file.writelines(store_tuple[0])
    file.write("\n")
    file.write("Books:\n")
    file.writelines(store_tuple[1])

def run():
  data = search("books.txt")
  save("section-books.txt", data)

run()


