"""
Programming for Social Science September '17
Agent Class
@author: Keiran Suchak
"""

# Imports
import random as rand
import math

# Agent class
class Agent():
    """
    Agent class:
    A class to capture the behaviour of an abstract agent interacting with a given environment.

    Constructor takes argument:
        env -- a list of lists characterising the 2-d landscape in which the agent exists (no default).
        agents -- a list of agents in the environment.
        neighbourhood -- the cartesian distance within which an agent will consider sharing its store.

    Agent characteristics:
        - store
        - x-coordinate
        - y-coordinate

    Agent behaviours include:
        - move
        - eat
        - sick
    """
    # Constructor methods
    def __init__(self, env, agents, neighbourhood):
        self._environment = env
        self._store = 0
        self._envWidth = len(env[0])   ## Assume that all rows are the same width
        self._envHeight = len(env)
        self._x = rand.randint(0,self._envWidth)
        self._y = rand.randint(0,self._envHeight)
        self._agents = agents
        self._neighbourhood = neighbourhood

    # Accessor methods
    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getStore(self):
        return self._store

    def getNeighbourhood(self):
        return self._neighbourhood
    
    # Modifier methods
    def setX(self, inputX):
        self._x = inputX

    def setY(self, inputY):
        self._y = inputY

    def setStore(self, inputStore):
        self._store = inputStore

    def setNeighbourhood(self, inputNeighbourhood):
        self._neighbourhood = inputNeighbourhood

    def move(self):
        # Move x
        if rand.random() < 0.5:
            self._x = (self._x + 1) % self._envWidth
        else:
            self._x = (self._x - 1) % self._envWidth

        # Move y
        if rand.random() < 0.5:
            self._y = (self._y + 1) % self._envHeight
        else:
            self._y = (self._y - 1) % self._envHeight

    def eat(self):
        if self._environment[self._y][self._x] > 10:
            self._environment[self._y][self._x] -= 10
            self._store += 10
        # Eat less if there isn't much left (but obviously can't eat if there's 0 food)
        elif self._environment[self._y][self._x] > 0:
            self._environment[self._y][self._x] -= 1
            self._store += 1

    def sick(self, quantity=50):
        # Avoid using too high a quantity to throw up, as this can max out the matplotlib colour scale
        if self._store > 1000:
            self._environment[self._y][self._x] += quantity
            self._store -= quantity

    def interact(self):
        self.move()
        self.eat()
        self.shareWithNeighbours()

    # Calculate cartesian distance between self and other agent
    def _distanceBetween(self, otherAgent):
        return math.sqrt((self._x - otherAgent.x)**2 + (self._y - otherAgent.y)**2)

    def shareWithNeighbours(self):
        for agent in filter(lambda a: a != self, self._agents):
            distance = self._distanceBetween(agent)
            # Only share with other agents within neighbourhood
            if distance <= self._neighbourhood:
                # Share stores equally
                average = (self._store + agent.store)/2
                self._store = average
                agent.store = average

    # Properties
    x = property(fget=getX, fset=setX, doc='The x-coordinate of the agent')
    y = property(fget=getY, fset=setY, doc='The y-coordinate of the agent')
    store = property(fget=getStore, fset=setStore, doc='The store of the agent')
    neighbourhood = property(fget=getNeighbourhood, fset=setNeighbourhood, doc='The neighbourhood of the agent')

    # Agent string
    def __str__(self):
        return 'Agent(x-coordinate={0}, y-coordinate={1}, store={2})'.format(self._x, self._y, self._store)
