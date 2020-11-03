import csv

def search(file_name):
  print("Searching...")
  data = {}
  with open(file_name) as file:
    for line in file:
      if line.startswith("Section"):
        section_split = line.split(":")
        section = section_split[1].replace('\n','')
        book_list = []
      else:
        book_list.append(line.replace('\n',''))
        book_str = ''
        if len(book_list) == 1:
          book_str = book_list[0]
        else:
          for i in range (len(book_list)-1):
            book_str += book_list[i] + ', '
          book_str += book_list[-1]
        data[section] = book_str

  print("...Done!")
  print(data)
  return data

def run():
  data = search("books.txt")
  with open("generated.csv", "w") as file:
    writer = csv.writer(file)
    for key, value in data.items():
       writer.writerow([key, value])

run()


