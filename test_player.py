import unittest
from block import Block
from player import Player

class TestPlayer(unittest.TestCase):

	def test_add_block(self):
		L = Block('red', [(0,0), (0,1), (0,2), (1,0)])
		player1 = Player('red',(-10,-10))
		player1.add_block(L)
		self.assertIn(L, player1.blocks)
		self.assertEqual(player1.blocks, [L])

	def test_remove_block(self):
		L = Block('red', [(0,0), (0,1), (0,2), (1,0)])
		L2 = Block('red', [(0,0), (0,1), (0,2), (1,0)])
		player1 = Player('red',(-10,-10))
		player1.add_block(L)
		player1.add_block(L2)
		self.assertEqual(player1.blocks, [L, L2])
		player1.remove_block(L)
		self.assertEqual(player1.blocks, [L2])
		#self.assertRaises(ValueError, player1.remove_block(L))



if __name__ == '__main__':
	unittest.main()


