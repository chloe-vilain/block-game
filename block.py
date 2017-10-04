import unittest

class Block(object):
	"""A block object with attributes 
	color: a string
	position: array of tuples, with each tuple 
	representing the position of one square in the block.
	"""
	def __init__(self, color, positions):
		self.color = color
		self.positions = positions

	def rotate(self, direction):
		if direction == 'left':
			self.positions = [(position[1] * -1, position[0]) for position in self.positions]
		elif direction == 'right':
			self.positions = [(position[1], position[0] * -1) for position in self.positions]
		else:
			raise ValueError('Invalid direction') 

	def reflect(self, axis):
		if axis == 'x':
			self.positions = [(position[0], position[1] * -1) for position in self.positions]
		elif axis == 'y':
			self.positions = [(position[0]* -1, position[1]) for position in self.positions]
		else:
			raise ValueError('Invalid axis')


"""class Board(object):

	def __init__(self, y=20, x=20):
		self.blocks = {}

	def add_block(self,block,orientation,location):
		self.blocks[]"""

def tests():
	L = Block('red', [(0,0), (0,1), (0,2), (1,0)])
	print(L)
	print(L.positions)
	print(L.color)
	for i in range(4):
		L.rotate('left')
		print(L.positions)
	for i in range(4):
		L.rotate('right')
		print(L.positions)
	for i in range(2):
		L.reflect('x')
		print(L.positions)
	for i in range(2):
		L.reflect('y')
		print(L.positions)


tests()
