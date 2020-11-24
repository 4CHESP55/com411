import matplotlib.pyplot as plt   
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
dicts = []

def init():
  dicts.extend([
	{
		'x':[1, 2, 2, 1, 1],
		'y':[1, 1, 2, 2, 1]
	},
	{
		'x':[1, 3, 3, 1, 1],
		'y':[1, 1, 3, 3, 1]
	},
	{
		'x':[1, 4, 4, 1, 1],
		'y':[1, 1, 4, 4, 1]
	}
  ])

def animate(frame):  
  ax.cla()  
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  square_size = frame % 3
  ax.plot(np.array(dicts[square_size]['x'] + np.array(frame % 5)), np.array(dicts[square_size]['y'] + np.array(frame % 7)), 'r-')

def run():
  init()
  simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show()

run()