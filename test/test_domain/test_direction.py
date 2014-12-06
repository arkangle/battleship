
import unittest
from domain.direction import *
from domain.coordinate import Coordinate

class TestDirection(unittest.TestCase):
    def testHorizFactory(self):
        Dir = Direction.Factory('Horiz')
        self.assertIsInstance(Dir,HorizontalDirection)

    def testVertFactory(self):
        Dir = Direction.Factory('Vert')
        self.assertIsInstance(Dir,VerticalDirection)

class TestHorizontalDirection(unittest.TestCase):
    def setUp(self):
        self.Dir = HorizontalDirection()

    def testNextXY(self):
        x_y = self.Dir.nextXY((3,3))
        self.assertEqual(x_y,(4,3))

class TestVerticalDirection(unittest.TestCase):
    def setUp(self):
        self.Dir = VerticalDirection()

    def testNextXY(self):
        x_y = self.Dir.nextXY((3,3))
        self.assertEqual(x_y,(3,4))
