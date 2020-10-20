def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods), max(likelihoods))

def run():
  print("Minimum likelihood of falling: {}%".format(min(likelihood())))
  print("Maximum likelihood of falling: {}%".format(max(likelihood())))

run()