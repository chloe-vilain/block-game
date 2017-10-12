import unittest
from block import Block
from board import Board

class TestBlock(unittest.TestCase):

	def test_add_block(self):
		g = Board()
		l = Block('red', [(0, 0), (0, 1), (0, 2), (1, 0)])
		g.add_block(l, (7, 7))
		self.assertEqual(g.grid[(7,7)],'red')
		self.assertEqual(g.grid[(7,8)], 'red')
		self.assertEqual(g.grid[(7,9)], 'red')
		self.assertEqual(g.grid[(8,7)], 'red')
		self.assertNotEqual(g.grid[(7,7)], 'blue')
		self.assertNotIn((9,9), g.grid.keys())

	def test_can_add_block(self):
		g = Board()
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
		self.assertFalse(g.can_add_block(o, (0,0), True))
		self.assertTrue(g.can_add_block(o, (-10,-10), True))

if __name__ == '__main__':
	unittest.main()