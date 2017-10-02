## Agent Practical 6 of 9
vis = True

## Imports:
import random as rand
import math
import operator as op
import matplotlib.pyplot as plt
import agentframework
import csv

## Constants:
num_of_agents = 10
num_of_iterations = 10000
agents = list()

## Functions:
def distance_between(agent0, agent1):
    return math.sqrt((agent0.x - agent1.x)**2 + (agent0.y - agent1.y)**2)

## Main:
# Read in data
environment = list()
with open('in.txt', newline='') as f:
    csvreader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in csvreader:
        row_list = list()
        for item in row:
            row_list.append(int(item))
        environment.append(row_list)

#  Plot environment
if vis:
    plt.xlim(0,len(environment[0]))
    plt.ylim(0,len(environment))
    plt.imshow(environment)
    plt.show()

# Make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# Move agents
for j in range(num_of_iterations):
    for agent in agents:
        agent.move()
        agent.eat()
        agent.sick()

# Write out the end environment
with open('out.txt', 'w', newline='') as g:
    csvwriter = csv.writer(g, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)

# Write agent stores

# Plotting
if vis:
    plt.xlim(0,len(environment[0]))
    plt.ylim(0,len(environment))
    plt.imshow(environment)
    for agent in agents:
        plt.scatter(agent.x, agent.y)
    plt.show()

# # Calculate distances
# for j in range(len(agents)):
#   for i in range(j+1, len(agents)):
#       distance = distance_between(agents[j], agents[i])
#       print('Distance between agent {0} and agent {1} = {2}'.format(j, i, distance))
