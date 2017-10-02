## Agent Practical 7 of 9
## Visualisations on/off
vis = False

## Imports:
import random as rand
import math
import operator as op
import matplotlib.pyplot as plt
import agentframework
import csv
import sys

## Constants:
if len(sys.argv) != 4:
    print('Incorrect number of args - reverting to default args')
    num_of_agents = 10
    num_of_iterations = 100
    neighbourhood = 20
else:
    num_of_agents = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])
print('Running for {0} agents, {1} iterations, neighbourhood = {2}'.format(num_of_agents, num_of_iterations, neighbourhood))

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

# Plot initial environment
if vis:
    plt.xlim(0,len(environment[0]))
    plt.ylim(0,len(environment))
    plt.imshow(environment)
    plt.show()

# Make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move agents
for j in range(num_of_iterations):
    # Shuffle order of agents in each iteration
    rand.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        # agent.sick()
        agent.share_with_neighbours(neighbourhood)

# Write out the final environment
with open('out.txt', 'w', newline='') as g:
    csvwriter = csv.writer(g, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)

# Write out final agent stores
with open('stores.txt', 'a') as h:
    stores = ','.join([str(agent.store) for agent in agents])
    h.write('{0}\n'.format(stores))

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
