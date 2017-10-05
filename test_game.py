import unittest
from block import Block
from game import Game

class TestBlock(unittest.TestCase):

	def test_add_block(self):
		g = Game()
		l = Block('red', [(0, 0), (0, 1), (0, 2), (1, 0)])
		g.add_block(l, (7, 7))
		self.assertEqual(g.board[(7,7)],'red')
		self.assertEqual(g.board[(7,8)], 'red')
		self.assertEqual(g.board[(7,9)], 'red')
		self.assertEqual(g.board[(8,7)], 'red')
		self.assertNotEqual(g.board[(7,7)], 'blue')
		self.assertNotIn((9,9), g.board.keys())

	def test_can_add_block(self):
		g = Game()
		l = Block('red', [(0, 0), (0, 1), (0, 2), (1, 0)])
		o = Block('red', [(0, 0), (0, 1), (1, 0), (1, 1)])
		o2 = Block('blue', [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)])
		g.add_block(l, (7, 7))
		self.assertFalse(g.can_add_block(o, (8, 10)))
		self.assertFalse(g.can_add_block(o, (7, 7)))
		self.assertFalse(g.can_add_block(o, (8, 8)))
		self.assertTrue(g.can_add_block(o, (5, 5)))
		self.assertFalse(g.can_add_block(o2, (5, 5)))
		self.assertFalse(g.can_add_block(o, (0,0)))

if __name__ == '__main__':
	unittest.main()