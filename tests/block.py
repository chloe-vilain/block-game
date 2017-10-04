import unittest
import Block

class TestBlock(unittest.TestCase):

	def test_rotation(self):
		L = Block.Block('red', [(0,0), (0,1), (0,2), (1,0)])
		self.assertEqual(L.position, [(0,0), (0,1), (0,2), (1,0)])

if __name__ == '__main__':
	unittest.main()