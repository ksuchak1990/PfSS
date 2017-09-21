## Agent Framework
import random as rand
class Agent():
	# Constructor methods
	def __init__(self):
		self._x = rand.randint(0,100)
		self._y = rand.randint(0,100)

	# Accessor methods
	def getx(self):
		return self._x

	def gety(self):
		return self._y
	
	# Modifier methods
	def setx(self, input_x):
		self._x = input_x

	def sety(self, input_y):
		self._y = input_y

	def move(self):
		# Move x
		if rand.random() < 0.5:
			self._x = (self._x + 1) % 100
		else:
			self._x = (self._x - 1) % 100

		# Move y
		if rand.random() < 0.5:
			self._y = (self._y + 1) % 100
		else:
			self._y = (self._y - 1) % 100

	# Properties
	x = property(fget=getx, fset=setx, doc="The x-coordinate of the agent")
	y = property(fget=gety, fset=sety, doc="The y-coordinate of the agent")

