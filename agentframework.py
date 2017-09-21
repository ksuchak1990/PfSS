## Agent Framework
import random as rand
class Agent():
	## Constructor methods
	def __init__(self, env):
		self._environment = env
		self._store = 0
		self._env_width = len(env[0])
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

	# Sick
	def sick(self):
		if self._store > 1000:
			self._environment[self._y][self._x] += self._store
			self._store = 0

	## Properties
	x = property(fget=getx, fset=setx, doc='The x-coordinate of the agent')
	y = property(fget=gety, fset=sety, doc='The y-coordinate of the agent')
	store = property(fget=getstore, fset=setstore, doc='The store of the agent')

	def __str__(self):
		return 'x-coordinate = {0}, y-coordinate = {1}, store = {2}'.format(self._x, self._y, self._store)
