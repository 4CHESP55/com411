def observed():
  observations = []
  for i in range (0,7,1):
    print("Please enter an observation: ")
    observations.append(input())
  return observations

def run():
  print("Counting observations...")
  obs_list = observed()
  observations = set()
  for element in obs_list:
    num = obs_list.count(element)
    observations.add((element, num))
  for element in observations:
    s = ""
    if element[1] > 1:
      s = "s"
    print(element[0] + " observed " + str(element[1]) + " time" + s + ".")

run()