## Agent Practical 5 of 9

## Imports:
import random as rand
import math
import operator as op
import matplotlib.pyplot as py
import agentframework

num_of_agents = 10
num_of_iterations = 100
agents = list()

def distance_between(agent0, agent1):
	return math.sqrt((agent0.x - agent1.x)**2 + (agent0.y - agent1.y)**2)

# Make agents
for i in range(num_of_agents):
	agents.append(agentframework.Agent())

# Move agents
for j in range(num_of_iterations):
	for i in range(num_of_agents):
		agents[i].move()

# Plotting
py.xlim(0,99)
py.ylim(0,99)
for i in range(num_of_agents):
	py.scatter(agents[i].x, agents[i].y)
py.show()

# Calculate distances
for j in range(len(agents)):
	for i in range(j+1, len(agents)):
		distance = distance_between(agents[j], agents[i])
		print('Distance between agent {0} and agent {1} = {2}'.format(j, i, distance))
