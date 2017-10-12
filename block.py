
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


