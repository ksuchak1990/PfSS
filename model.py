## Agent Practical 3 of 9

## Imports:
import random as rand
import math
import operator as op
import matplotlib.pyplot as py

num_of_agents = 10
num_of_iterations = 100
agents = list()

## Model:
# Provide each agent with an initial x-y coordinate
for i in range(num_of_agents):
	agents.append([rand.randint(0,100), rand.randint(0, 100)])

# Make each agent move an arbitrary number of times
for j in range(num_of_iterations):
	for i in range(num_of_agents):
		# Change x and y based on random numbers.
		if rand.random() < 0.5:
			agents[i][0] = (agents[i][0] + 1) % 100
		else:
			agents[i][0] = (agents[i][0] - 1) % 100

		if rand.random() < 0.5:
			agents[i][1] = (agents[i][1] + 1) % 100
		else:
			agents[i][1] = (agents[i][1] - 1) % 100

# A little bit of plotting
py.xlim(0,99)
py.ylim(0,99)
for agent in agents:
	py.scatter(agent[0], agent[1])
py.show()
