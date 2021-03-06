
import unittest
from domain.coordinate import Coordinate
from domain.direction import *

class TestCoordinate(unittest.TestCase):
    def testXandY(self):
        coor = Coordinate(1,2)
        self.assertEqual(1,coor.x)
        self.assertEqual(2,coor.y)

    def testGetX(self):
        coor = Coordinate(1,2)
        self.assertEqual(1,coor.getX())

    def testGetY(self):
        coor = Coordinate(1,2)
        self.assertEqual(2,coor.getY())

    def testGetXY(self):
        coor = Coordinate(1,2)
        self.assertEqual((1,2),coor.getXY())

    def testGetRow(self):
        coor = Coordinate(1,2)
        self.assertEqual("C",coor.getRow())

    def testGetColumn(self):
        coor = Coordinate(1,2)
        self.assertEqual(2,coor.getColumn())

    def testGetRowColumn(self):
        coor = Coordinate(1,2)
        self.assertEqual(("C",2),coor.getRowColumn())

    def testGetRowColumnJ10(self):
        coor = Coordinate.Factory("J",10)
        self.assertEqual(("J",10),coor.getRowColumn())

    def testEquality(self):
        coor1 = Coordinate.Factory("J",10)
        coor2 = Coordinate(9,9)
        self.assertTrue(coor1==coor2);

    def testNotEquality(self):
        coor1 = Coordinate.Factory("J",10)
        coor2 = Coordinate(1,9)
        self.assertTrue(coor1!=coor2);

    def testFactoryA1(self):
        coor = Coordinate.Factory("A",1)
        self.assertEqual(0,coor.getX())
        self.assertEqual(0,coor.getY())

    def testFactoryE5(self):
        coor = Coordinate.Factory("E",5)
        self.assertEqual(4,coor.getX())
        self.assertEqual(4,coor.getY())

    def testFactoryJ10(self):
        coor = Coordinate.Factory("J",10)
        self.assertEqual(9,coor.getX())
        self.assertEqual(9,coor.getY())

    def testFactoryA10(self):
        coor = Coordinate.Factory("A",10)
        self.assertEqual(9,coor.getX())
        self.assertEqual(0,coor.getY())

    def testFactoryJ1(self):
        coor = Coordinate.Factory("J",1)
        self.assertEqual(0,coor.getX())
        self.assertEqual(9,coor.getY())

    def testFactoryE1(self):
        coor = Coordinate.Factory("E",1)
        self.assertEqual(0,coor.getX())
        self.assertEqual(4,coor.getY())

    def testInvalidArgumentsFactory(self):
        self.assertRaises(ValueError,Coordinate.Factory,"A",11)
        self.assertRaises(ValueError,Coordinate.Factory,"K",0)
        self.assertRaises(ValueError,Coordinate.Factory,"Z",11)

    def testRange(self):
        tests = [Coordinate(3,3),Coordinate(4,3),Coordinate(5,3)]
        Horiz = HorizontalDirection();
        Coor = Coordinate(3,3)
        Range = Coor.range(Horiz,3)
        self.assertEqual(tests,Range)
