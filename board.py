import math

class Board(object):
	"""
	This represents a block game's data
	PERF: consider the space/ time tradeoffs of
	calling get_block_coordinates every time
	versus saving it as a variable.

	"""

	def __init__(self, dimensions = (20, 20)):
		self.grid = {}
		self.x_min = -1*int(math.floor(dimensions[0]/2))
		self.x_max = int(math.ceil(dimensions[0]/2))
		self.y_min = -1*int(math.floor(dimensions[1]/2))
		self.y_max = int(math.ceil(dimensions[1]/2))


	def add_block(self, block, location):
		for position in self.get_block_coordinates(block, location):
			self.grid[position] = block.color


	def can_add_block(self, block, location, first_turn = False, orgin = (-10,-10)):
		"""
		Three cases must always be met:
		New block must fit entirely in the grid 
		New block must not overlap any existing blocks
		New block must not touch any block of the same color on an edge
		If it is NOT the first turn:
		New block must touch a block of the same color on a cornet
		If it is the first turn:
		Block must be placed at that player's orgin
		"""
		coordinates = self.get_block_coordinates(block, location)
		if first_turn == False:
			return self.is_in_range(coordinates) and self.does_overlap(coordinates) and self.touches_same_color(block, location) and self.corners_same_color(block, location)
		else:
			return self.is_in_range(coordinates) and self.does_overlap(coordinates) and self.touches_same_color(block, location) and self.is_at_orgin(coordinates, orgin)
	
	def is_at_orgin(self, coordinates, orgin):
		if orgin in coordinates:
			return True
		return False 

	def is_in_range(self, coordinates):
		for position in coordinates:
			if self.x_min > position[0] or self.y_min > position[1] or self.x_max < position[0] or self.y_max < position[1]:
				return False
		return True

	def does_overlap(self, coordinates):
		for position in coordinates:
			if position in self.grid.keys():
				return False
		return True

	def touches_same_color(self, block, location):
		for position in self.get_adjacencies(block, location):
			if position in self.grid and self.grid[position] == block.color:
				return False
		return True

	def corners_same_color(self, block, location):
		for position in self.get_corners(block, location):
				if position in self.grid and self.grid[position] == block.color:
					return True
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















