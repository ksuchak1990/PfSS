## Agent Practical 1 of 9 - Data Variables

## Imports:
import random as rand
import math
import operator as op
import matplotlib.pyplot as py

agents = list()

## Model:
# # Make a x variable.
# # Make a y variable.
agents.append([rand.randint(0,100), rand.randint(0,100)])

# Test that they've been assigned properly
print('x0 = {0}, y0 = {1}'.format(agents[0][0], agents[0][1]))

# Change x and y based on random numbers.
random_number = rand.random()
if random_number < 0.5:
	agents[0][0] += 1
else:
	agents[0][0] -= 1

print('random_number = {0}, therefore new x0 = {1}'.format(random_number, agents[0][0]))

random_number = rand.random()
if random_number < 0.5:
	agents[0][1] += 1
else:
	agents[0][1] -= 1

print('random_number = {0}, therefore new y0 = {1}'.format(random_number, agents[0][1]))

random_number = rand.random()
if random_number < 0.5:
	agents[0][0] += 1
else:
	agents[0][0] -= 1

print('random_number = {0}, therefore new x0 = {1}'.format(random_number, agents[0][0]))

random_number = rand.random()
if random_number < 0.5:
	agents[0][1] += 1
else:
	agents[0][1] -= 1

print('random_number = {0}, therefore new y0 = {1}'.format(random_number, agents[0][1]))




# Make a second set of x and ys, and make these change randomly as well.

# Make a x variable.
# Make a y variable.
agents.append([rand.randint(0,100), rand.randint(0,100)])

# Test that they've been assigned properly
print('x1 = {0}, y1 = {1}'.format(agents[1][0], agents[1][1]))

# Change x and y based on random numbers.
random_number = rand.random()
if random_number < 0.5:
	agents[1][0] += 1
else:
	agents[1][0] -= 1

print('random_number = {0}, therefore new x1 = {1}'.format(random_number, agents[1][0]))

random_number = rand.random()
if random_number < 0.5:
	agents[1][1] += 1
else:
	agents[1][1] -= 1

print('random_number = {0}, therefore new y1 = {1}'.format(random_number, agents[1][1]))

random_number = rand.random()
if random_number < 0.5:
	agents[1][0] += 1
else:
	agents[1][0] -= 1

print('random_number = {0}, therefore new x1 = {1}'.format(random_number, agents[1][0]))

random_number = rand.random()
if random_number < 0.5:
	agents[1][1] += 1
else:
	agents[1][1] -= 1

print('random_number = {0}, therefore new y1 = {1}'.format(random_number, agents[1][1]))

print(agents)

# Work out the distance between two setes of x and ys.
answer = math.sqrt((agents[1][0]-agents[0][0])**2 + (agents[1][1]-agents[0][1])**2)
print(answer)

# A little bit of plotting
py.xlim(0,99)
py.ylim(0,99)
m = max(agents, key=op.itemgetter(1))
print(m)
py.scatter(agents[0][0], agents[0][1])
py.scatter(agents[1][0], agents[1][1])
py.scatter(m[0], m[1], color='red')
py.show()
