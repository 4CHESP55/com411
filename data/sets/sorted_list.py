def observed():
  observations = []
  for i in range (0,5,1):
    print("Please enter an observation: ")
    observations.append(input())
  return observations

def remove_observations(obs_list):
  print ("Do you wish to remove an observation (yes/no)?")
  if input() == "yes":
    print("What observation do you wish to remove?")
    item_remove = input()
    obs_list.remove(item_remove)
  else:
    print("Nothing to remove")
  return obs_list

def run():
  obs_list = remove_observations(observed())
  observations = set()
  for element in obs_list:
    num = obs_list.count(element)
    observations.add((element, num))
  sorted_obs = sorted(observations)
  for element in sorted_obs:
    s = ""
    if element[1] > 1:
      s = "s"
    print(element[0] + " observed " + str(element[1]) + " time" + s + ".")

run()