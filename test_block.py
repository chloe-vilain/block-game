import unittest
from block import Block

class TestBlock(unittest.TestCase):

	def test_rotation(self):
		L = Block('red', [(0,0), (0,1), (0,2), (1,0)])
		self.assertEqual(L.positions, [(0,0), (0,1), (0,2), (1,0)])
		L.rotate('left')
		self.assertEqual(L.positions, [(0, 0), (-1, 0), (-2, 0), (0, 1)])
		L.rotate('left')
		self.assertEqual(L.positions,[(0, 0), (0, -1), (0, -2), (-1, 0)])
		L.rotate('left')
		self.assertEqual(L.positions,[(0, 0), (1, 0), (2, 0), (0, -1)])
		L.rotate('left')
		self.assertEqual(L.positions,[(0, 0), (0, 1), (0, 2), (1, 0)])
		L.rotate('right')
		self.assertEqual(L.positions, [(0,0), (1, 0), (2, 0), (0, -1)])
		L.rotate('right')
		self.assertEqual(L.positions, [(0, 0), (0, -1), (0, -2), (-1, 0)])
		L.rotate('right')
		self.assertEqual(L.positions, [(0, 0), (-1, 0), (-2, 0), (0, 1)])
		L.rotate('right')
		self.assertEqual(L.positions, [(0, 0), (0, 1), (0, 2), (1, 0)])

	def test_reflection(self):
		L = Block('red', [(0,0), (0,1), (0,2), (1,0)])
		L.reflect('x')
		self.assertEqual(L.positions, [(0,0),(0,-1),(0,-2),(1,0)])
		L.reflect('x')
		self.assertEqual(L.positions, [(0,0), (0,1), (0,2), (1,0)])
		L.reflect('y')
		self.assertEqual(L.positions, [(0,0),(0,1),(0,2),(-1,0)])
		L.reflect('y')
		self.assertEqual(L.positions, [(0,0), (0,1), (0,2), (1,0)])


if __name__ == '__main__':
	unittest.main()