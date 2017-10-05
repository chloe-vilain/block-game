import math

class Game(object):
	"""
	This represents a block game's data
	Not to be confused with the GUI methods/ loops
	To be renamed later
	"""

	def __init__(self, dimensions = (20, 20)):
		self.board = {}
		self.x_min = -1*int(math.floor(dimensions[0]/2))
		self.x_max = int(math.ceil(dimensions[0]/2))
		self.y_min = -1*int(math.floor(dimensions[1]/2))
		self.y_max = int(math.ceil(dimensions[1]/2))


	def add_block(self, block, location):
		for position in self.get_block_coordinates(block, location):
			self.board[position] = block.color


	def can_add_block(self, block, location):
		"""
		Four cases must be met:
		New block must fit entirely in the board 
		New block must not overlap any existing blocks
		New block must not touch any block of the same color on an edge
		New block must touch a block of the same color on a cornet
		"""
		coordinates = self.get_block_coordinates(block, location)
		for position in coordinates:
			if self.x_min > position[0] or self.y_min > position[1] or self.x_max < position[0] or self.y_max < position[1]:
				#print "Out of range"
				return False
		for position in coordinates:
			if position in self.board.keys():
				#print "Overlaps existing block"
				return False
		for position in self.get_adjacencies(block, location):
			if position in self.board and self.board[position] == block.color:
				#print "Adjacent to a block of the same color"
				return False
		for position in self.get_corners(block, location):
			if position in self.board and self.board[position] == block.color:
				return True
		#print "Not cornering a block of the same color"
		return False 

	def get_block_coordinates(self, block, location):
		return [(position[0] + location[0], position[1]+location[1]) for position in block.positions] 

	def get_adjacencies(self, block, location):
		"""
		This set includes out-of-bound locations
		and locations overlapping an existing block
		"""
		adjacencies = set()
		for position in self.get_block_coordinates(block,location):
			adjacencies.add((position[0]+1, position[1]))
			adjacencies.add((position[0]-1, position[1]))
			adjacencies.add((position[0], position[1]+1))
			adjacencies.add((position[0], position[1]-1))
		return adjacencies

	def get_corners(self, block, location):
		corners = set()
		for position in self.get_block_coordinates(block, location):
			corners.add((position[0]+1, position[1]+1))
			corners.add((position[0]+1, position[1]-1))
			corners.add((position[0]-1, position[1]+1))
			corners.add((position[0]-1, position[1]-1))
		return corners













