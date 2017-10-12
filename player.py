from block import Block 

class Player(object):
	"""
	This represents a player in the game
	PERF: Consider data structures other than
	array to improve performance  - block list does not 
	need to be indexed)

	"""

	def __init__(self, color, orgin_coordinates):
		"""
		Instanciates a player
		Returns null
		"""
		self.color = color
		self.orgin = orgin_coordinates
		self.blocks = []

	def add_block(self, block):
		"""
		Adds a block to the player's hand
		"""
		self.blocks.append(block)

	def remove_block(self, block):
		"""
		Removes block from the player's hand
		"""
		self.blocks.remove(block)
		
