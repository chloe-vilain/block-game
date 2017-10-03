
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
			for i in range(len(self.positions)):
				self.positions[i]=(self.positions[i][1]*-1,self.positions[i][0])
		elif direction == 'right':
			for i in range(len(self.positions)):
				self.positions[i]=(self.positions[i][1],self.positions[i][0]*-1)


	def reflect(self, axis):
		if axis == 'x':
			for i in range(len(self.positions)):
				self.positions[i]=(self.positions[i][0],self.positions[i][1]*-1)
		elif axis == 'y':
			for i in range(len(self.positions)):
				self.positions[i]=(self.positions[i][0]*-1,self.positions[i][1])





"""class Board(object):

	def __init__(self, y=20, x=20):
		self.blocks = {}

	def add_block(self,block,orientation,location):
		self.blocks[]"""


def tests():
	L = Block("red",[(0,0),(0,1),(0,2),(1,0)])
	print (L)
	print (L.positions)
	print (L.color)
	for i in range(4):
		L.rotate('left')
		print (L.positions)
	for i in range(4):
		L.rotate('right')
		print (L.positions)
	for i in range(2):
		L.reflect('x')
		print (L.positions)
	for i in range(2):
		L.reflect('y')
		print (L.positions)


tests()
