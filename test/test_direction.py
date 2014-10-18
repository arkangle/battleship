
import unittest
from domain.direction import *

class TestDirection(unittest.TestCase):
    def testHorizFactory(self):
        Dir = Direction.Factory('Horiz')
        self.assertIsInstance(Dir,HorizontalDirection)

    def testVertFactory(self):
        Dir = Direction.Factory('Vert')
        self.assertIsInstance(Dir,VerticalDirection)

class TestHorizontalDirection(unittest.TestCase):
    def testGetEndXY(self):
        Dir = HorizontalDirection()
        end_x_y = Dir.getEndXY((1,2),3)
        self.assertEquals((4,2),end_x_y)

class TestVerticalDirection(unittest.TestCase):
    def testGetEndXY(self):
        Dir = VerticalDirection()
        end_x_y = Dir.getEndXY((1,2),3)
        self.assertEquals((1,5),end_x_y)

