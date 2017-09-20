## Agent Practical 4 of 9

## Imports:
import random as rand
import math
import operator as op
import matplotlib.pyplot as py
import datetime

num_of_agents = 3
num_of_iterations = 100
board_size = 100
time_record = list()

## Functions:
# Distance Functions
def distanceBetween(agent0, agent1):
	return math.sqrt((agent0[0] - agent1[0])**2 + (agent0[1] - agent1[1])**2)

def distanceBetweenAgents(agents, verbose=False):
	output = list()
	for i in range(len(agents)):
		output.append(list())
		for j in range(i+1, len(agents)):
			distance = distanceBetween(agents[i], agents[j])
			if verbose:
				print('Distance between agents {0} and {1} = {2}'.format(i, j, distance))
			output[i].append(distance)
	return output

# Timing functions
def getTimeMS():
	dt = datetime.datetime.now()
	return dt.microsecond + (dt.second * 1000000) + (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)

# Plotting functions
def plotAgents(agents):
	py.xlim(0,99)
	py.ylim(0,99)
	for agent in agents:
		py.scatter(agent[0], agent[1])
	py.show()

# Movement functions
def moveAgents(a):
	for i in range(len(a)):
		for c in range(len(a[i])):
			if rand.random() < 0.5:
				a[i][c] = (a[i][c] + 1) % board_size
			else:
				a[i][c] = (a[i][c] - 1) % board_size
	return a

# Run function
def run(num, plotting=False):
	## Instantiate list of agents
	agents = list()

	# Make agents, and provide each one with an initial x-y coordinate	
	for i in range(num_of_agents):
		agents.append([rand.randint(0, board_size), rand.randint(0, board_size)])

	# Make each agent move an arbitrary number of times
	for j in range(num_of_iterations):
		agents = moveAgents(agents)

	# Calculate the distance between each distinct pair of agents
	distances = distanceBetweenAgents(agents)

	# for i in range(num_of_agents):
	# 	for j in range(i+1, num_of_agents):
	# 		print('Distance between agents {0} and {1} = {2}'.format(i, j, distanceBetween(agents[i], agents[j])))

	# Plot if required
	if plotting:
		plotAgents(agents)

## Main
for n in range(2,9):
	order = n/2
	num_of_agents = round(10**order)
	start = getTimeMS()
	run(num_of_agents)
	end = getTimeMS()
	time_taken = end - start
	print('Time taken for {0} agents = {1}'.format(num_of_agents, time_taken))
	time_record.append([order, time_taken])

for record in time_record:
	py.scatter(record[0], math.log(record[1]))
py.show()
