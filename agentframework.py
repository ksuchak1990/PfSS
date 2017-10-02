## Agent Framework

## Imports
import random as rand

## Define Agent class
class Agent():
    """
    Agent class:
    A class to capture the behaviour of an abstract agent interacting with a given environment.

    Constructor takes argument:
        env -- a list of lists characterising the 2-d landscape in which the agent exists (no default)

    Agent characteristics:
        - store
        - x coordinate
        - y coordinate

    Agent behaviours include:
        - move
        - eat
        - sick
    """
    ## Constructor methods
    def __init__(self, env):
        self._environment = env
        self._store = 0
        self._env_width = len(env[0])   ## Assue that all rows are the same width
        self._env_height = len(env)
        self._x = rand.randint(0,self._env_width)
        self._y = rand.randint(0,self._env_height)

    ## Accessor methods
    # Access x
    def getx(self):
        return self._x

    # Access y
    def gety(self):
        return self._y

    # Access store
    def getstore(self):
        return self._store
    
    ## Modifier methods
    # Modify x
    def setx(self, input_x):
        self._x = input_x

    # Modify y
    def sety(self, input_y):
        self._y = input_y

    # Modify store
    def setstore(self, input_store):
        self._store = input_store

    # Move
    def move(self):
        # Move x
        if rand.random() < 0.5:
            self._x = (self._x + 1) % self._env_width
        else:
            self._x = (self._x - 1) % self._env_width

        # Move y
        if rand.random() < 0.5:
            self._y = (self._y + 1) % self._env_height
        else:
            self._y = (self._y - 1) % self._env_height

    # Eat
    def eat(self):
        if self._environment[self._y][self._x] > 10:
            self._environment[self._y][self._x] -= 10
            self._store += 10
        # Eat less if there isn't much left (but obviously can't eat if there's 0 food)
        elif self._environment[self._y][self._x] > 0:
            self._environment[self._y][self._x] -= 1
            self._store += 1

    # Sick
    def sick(self, quantity=50):
        # Avoid using to high a quantity to throw up, as this can max out the matplotlib colour scale
        if self._store > 1000:
            self._environment[self._y][self._x] += quantity
            self._store -= quantity

    ## Properties
    x = property(fget=getx, fset=setx, doc='The x-coordinate of the agent')
    y = property(fget=gety, fset=sety, doc='The y-coordinate of the agent')
    store = property(fget=getstore, fset=setstore, doc='The store of the agent')

    def __str__(self):
        return 'x-coordinate = {0}, y-coordinate = {1}, store = {2}'.format(self._x, self._y, self._store)
