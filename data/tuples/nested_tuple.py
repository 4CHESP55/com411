def steps():
  percentages = [50, 38, 27, 99, 4]
  likelihoods = []
  for i in range (len(percentages)):
    step = "step " + str(i+1)
    step_likelihood = (step, percentages[i])
    likelihoods.append(step_likelihood)
  return likelihoods

def run():
  good_steps = []
  bad_steps = []
  for i in range (len(steps())):
    if steps()[i][-1] >= 50:
      bad_steps.append(steps()[i])
    else:
      good_steps.append(steps()[i])
  print("Good steps: {}, Bad steps: {}".format(len(good_steps), len(bad_steps)))

run()
