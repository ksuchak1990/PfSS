"""
Programming for Social Science September '17
Model runner script
@author: Keiran Suchak
"""

# Imports:
import csv
import sys
import random as rand
import matplotlib.pyplot as plt
from agentframework import Agent

# Set up constants:
# Visualisations and on/off
vis = True

# Command line args
if len(sys.argv) != 4:
    if len(sys.argv) == 1:
        print('No args provided - reverting to default args')
    else:
        print('Incorrect number of args - reverting to default args')
    num_of_agents = 10
    num_of_iterations = 100
    neighbourhood = 20
else:
    num_of_agents = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])
print('Running for {0} agents, {1} iterations, neighbourhood = {2}'.format(num_of_agents, num_of_iterations, neighbourhood))

# Functions
# Read in data
def readEnvironment(fileName="in.txt"):
    env = list()
    with open(fileName, newline='') as f:
        csvreader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in csvreader:
            row_list = list()
            for item in row:
                row_list.append(int(item))
            env.append(row_list)
    return env

# Write out the final environment
def writeEnvironment(data, fileName='out.txt'):
    with open(fileName, 'w', newline='') as g:
        csvwriter = csv.writer(g, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            csvwriter.writerow(row)

# Append final stores to file
def writeStores(data, fileName='stores.txt'):
    stores = ','.join([str(agent.store) for agent in data])
    with open('stores.txt', 'a') as h:
        h.write('{0}\n'.format(stores))

# # Update animation
# def update(frameNumber):
#     fig.clear()
#     for agent in agents:
#         agent.move()
#         plt.scatter(agent.x, agent.y)

# Main:
# Initialisation
agents = list()
environment = readEnvironment()
environmentWidth = len(environment[0])
environmentHeight = len(environment)

# Plot initial environment
if vis:
    plt.xlim(0, environmentWidth)
    plt.ylim(0, environmentHeight)
    plt.imshow(environment)
    plt.show()

# Make agents
for i in range(num_of_agents):
    agents.append(Agent(environment, agents, neighbourhood))

# Iterate agent interaction
for j in range(num_of_iterations):
    # Shuffle order of agents in each iteration
    rand.shuffle(agents)
    for agent in agents:
        agent.interact()

writeEnvironment(data=environment)
writeStores(data=agents)

# Plotting
if vis:
    plt.xlim(0, environmentWidth)
    plt.ylim(0, environmentHeight)
    plt.imshow(environment)
    for agent in agents:
        plt.scatter(agent.x, agent.y)
    plt.show()

# # Calculate distances
# for j in range(len(agents)):
#   for i in range(j+1, len(agents)):
#       distance = distance_between(agents[j], agents[i])
#       print('Distance between agent {0} and agent {1} = {2}'.format(j, i, distance))
