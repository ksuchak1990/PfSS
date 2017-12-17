# Imports
from agentframework import Agent
import random as rand
import math

# Class
class Sheep(Agent):
    def __init__(self, env, agents):
        super().__init__(env, agents)

    def share_with_neighbours(self, neighbourhood):
        # Loop through the agents in self.agents (except self)
        for agent in filter(lambda a: a != self and isinstance(a, Sheep), self._agents):
            # Calculate the distance between self and the current other agent:
            distance = self._distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Share stores equally
                average = (self.store + agent.store)/2
                self.store = average
                agent.store = average

    def __str__(self):
        return 'Sheep(x-coordinate={0}, y-coordinate={1}, store={2})'.format(self._x, self._y, self._store)
