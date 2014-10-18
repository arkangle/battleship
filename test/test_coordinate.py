
import unittest
from coordinate import Coordinate

class TestCoordinate(unittest.TestCase):
    def testXandY(self):
        coor = Coordinate((1,2))
        self.assertEquals(1,coor.x)
        self.assertEquals(2,coor.y)

    def testGetX(self):
        coor = Coordinate((1,2))
        self.assertEquals(1,coor.getX())

    def testGetY(self):
        coor = Coordinate((1,2))
        self.assertEquals(2,coor.getY())

    def testGetXY(self):
        coor = Coordinate((1,2))
        self.assertEquals((1,2),coor.getXY())

    def testGetRow(self):
        coor = Coordinate((1,2))
        self.assertEquals("C",coor.getRow())

    def testGetColumn(self):
        coor = Coordinate((1,2))
        self.assertEquals(2,coor.getColumn())

    def testGetRowColumn(self):
        coor = Coordinate((1,2))
        self.assertEquals(("C",2),coor.getRowColumn())

    def testGetRowColumnJ10(self):
        coor = Coordinate.Factory(("J",10))
        self.assertEquals(("J",10),coor.getRowColumn())

    def testFactoryA1(self):
        coor = Coordinate.Factory(("A",1))
        self.assertEquals(0,coor.getX())
        self.assertEquals(0,coor.getY())

    def testFactoryE5(self):
        coor = Coordinate.Factory(("E",5))
        self.assertEquals(4,coor.getX())
        self.assertEquals(4,coor.getY())

    def testFactoryJ10(self):
        coor = Coordinate.Factory(("J",10))
        self.assertEquals(9,coor.getX())
        self.assertEquals(9,coor.getY())

    def testFactoryA10(self):
        coor = Coordinate.Factory(("A",10))
        self.assertEquals(9,coor.getX())
        self.assertEquals(0,coor.getY())

    def testFactoryJ1(self):
        coor = Coordinate.Factory(("J",1))
        self.assertEquals(0,coor.getX())
        self.assertEquals(9,coor.getY())

    def testFactoryE1(self):
        coor = Coordinate.Factory(("E",1))
        self.assertEquals(0,coor.getX())
        self.assertEquals(4,coor.getY())

    def testInvalidArguments(self):
        self.assertRaises(ValueError,Coordinate,(-1,0))
        self.assertRaises(ValueError,Coordinate,(0,10))
        self.assertRaises(ValueError,Coordinate,(-1,10))

    def testInvalidArgumentsFactory(self):
        self.assertRaises(ValueError,Coordinate.Factory,("A",11))
        self.assertRaises(ValueError,Coordinate.Factory,("K",0))
        self.assertRaises(ValueError,Coordinate.Factory,("Z",11))

