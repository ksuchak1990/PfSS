# Imports
from agentframework import Agent
from Sheep import Sheep
import random as rand
import math

# Class
class Wolf(Agent):
    def __init__(self, env, agents):
        super().__init__(env, agents)

    def eat(self):
        neighbourhood = 20
        # Loop through the agents in self.agents (except self)
        for sheep in filter(lambda a: a != self and isinstance(a, Sheep), self._agents):
            # Calculate the distance between self and the current other agent:
            distance = self._distance_between(sheep)
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Wolf kills sheep, thus gaining its store
                self.store += sheep.store
                # Sheep dies, and is removed from list of agents
                self._agents = [agent for agent in self._agents if agent != sheep]


    def move(self):
        # Move x
        if rand.random() < 0.5:
            self._x = (self._x + 5) % self._env_width
        else:
            self._x = (self._x - 5) % self._env_width

        # Move y
        if rand.random() < 0.5:
            self._y = (self._y + 5) % self._env_height
        else:
            self._y = (self._y - 5) % self._env_height

    def __str__(self):
        return 'Wolf(x-coordinate={0}, y-coordinate={1}, store={2})'.format(self._x, self._y, self._store)
