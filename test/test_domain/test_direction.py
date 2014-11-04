
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
    def setUp(self):
        self.Dir = HorizontalDirection()

    def testGetEndXY(self):
        end_x_y = self.Dir.getEndXY((1,2),3)
        self.assertEqual((4,2),end_x_y)

    def testInBetween(self):
        origin_x_y = (1,2)
        length = 3
        for i in range(1,4):
            self.assertTrue(self.Dir.inBetween(origin_x_y,length,(i,2)))

    def testNotInBetween(self):
        origin_x_y = (1,2)
        length = 3
        self.assertFalse(self.Dir.inBetween(origin_x_y,length,(0,2)))
        self.assertFalse(self.Dir.inBetween(origin_x_y,length,(4,2)))

    def testGetRange(self):
        asserts = [(1,2),(2,2),(3,2)]
        origin_x_y = (1,2)
        length = 3
        range_x_y = self.Dir.getRange(origin_x_y,length)
        self.assertEqual(asserts,range_x_y)


class TestVerticalDirection(unittest.TestCase):
    def setUp(self):
        self.Dir = VerticalDirection()

    def testGetEndXY(self):
        end_x_y = self.Dir.getEndXY((1,2),3)
        self.assertEqual((1,5),end_x_y)

    def testInBetween(self):
        origin_x_y = (1,2)
        length = 3
        for i in range(2,5):
            self.assertTrue(self.Dir.inBetween(origin_x_y,length,(1,i)))

    def testNotInBetween(self):
        origin_x_y = (1,2)
        length = 3
        self.assertFalse(self.Dir.inBetween(origin_x_y,length,(1,1)))
        self.assertFalse(self.Dir.inBetween(origin_x_y,length,(2,3)))
        self.assertFalse(self.Dir.inBetween(origin_x_y,length,(1,5)))

    def testGetRange(self):
        asserts = [(1,2),(1,3),(1,4)]
        origin_x_y = (1,2)
        length = 3
        range_x_y = self.Dir.getRange(origin_x_y,length)
        self.assertEqual(asserts,range_x_y)
