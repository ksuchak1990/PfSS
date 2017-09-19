## Agent Practical 1 of 9 - Data Variables

## Imports:
import random as rand
import math

agents = list()

## Model:
# Make a x variable.
x0 = 50

# Make a y variable.
y0 = 50

# # Randomise start points instead
# x0 = rand.randomint(0,100)
# y0 = rand.randomint(0,100)

agents.append([x0, y0])

# Test that they've been assigned properly
print('x0 = {0}, y0 = {1}'.format(x0, y0))

# Change x and y based on random numbers.
random_number = rand.random()
if random_number < 0.5:
	x0 += 1
else:
	x0 -= 1

print('random_number = {0}, therefore new x0 = {1}'.format(random_number, x0))

random_number = rand.random()
if random_number < 0.5:
	y0 += 1
else:
	y0 -= 1

print('random_number = {0}, therefore new y0 = {1}'.format(random_number, y0))

random_number = rand.random()
if random_number < 0.5:
	x0 += 1
else:
	x0 -= 1

print('random_number = {0}, therefore new x0 = {1}'.format(random_number, x0))

random_number = rand.random()
if random_number < 0.5:
	y0 += 1
else:
	y0 -= 1

print('random_number = {0}, therefore new y0 = {1}'.format(random_number, y0))




# Make a second set of x and ys, and make these change randomly as well.

# Make a x variable.
x1 = 50

# Make a y variable.
y1 = 50

# # Randomise start points instead
# x1 = rand.randint(0,100)
# y1 = rand.randint(0,100)

# Test that they've been assigned properly
print('x1 = {0}, y1 = {1}'.format(x1, y1))

# Change x and y based on random numbers.
random_number = rand.random()
if random_number < 0.5:
	x1 += 1
else:
	x1 -= 1

print('random_number = {0}, therefore new x1 = {1}'.format(random_number, x1))

random_number = rand.random()
if random_number < 0.5:
	y1 += 1
else:
	y1 -= 1

print('random_number = {0}, therefore new y1 = {1}'.format(random_number, y1))

random_number = rand.random()
if random_number < 0.5:
	x1 += 1
else:
	x1 -= 1

print('random_number = {0}, therefore new x1 = {1}'.format(random_number, x1))

random_number = rand.random()
if random_number < 0.5:
	y1 += 1
else:
	y1 -= 1

print('random_number = {0}, therefore new y1 = {1}'.format(random_number, y1))

print(x0, y0, x1, y1)

# Work out the distance between two setes of x and ys.
answer = math.sqrt((x1-x0)**2 + (y1-y0)**2)
print(answer)
