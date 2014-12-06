
import unittest
from domain.ship import Ship
from domain.coordinate import Coordinate
from domain.direction import *
from domain.ship_type import *

class TestHorizShip(unittest.TestCase):
    def setUp(self):
        Origin = Coordinate(1,1)
        Dir = HorizontalDirection()
        Type = ShipType("HorizShip",4)
        self.TestShip = Ship(Type,Origin,Dir)

    def testIsHit(self):
        Coor = Coordinate(4,1)
        self.assertTrue(self.TestShip.isHit(Coor))

    def testIsNotHit(self):
        Coor = Coordinate(5,1)
        self.assertFalse(self.TestShip.isHit(Coor))

    def testShotAndHit(self):
        Coor = Coordinate(4,1)
        self.assertTrue(self.TestShip.fire(Coor))
        self.assertEqual(self.TestShip.getHits(),[Coor])

    def testShotAndMiss(self):
        Coor = Coordinate(5,1)
        self.assertFalse(self.TestShip.fire(Coor))
        self.assertEqual(self.TestShip.getHits(),[])

    def testGetHits(self):
        Coor = Coordinate(5,1)
        self.TestShip.fire(Coor)
        self.assertEqual(self.TestShip.getHits(),[])
        Coor = Coordinate(4,1)
        self.TestShip.fire(Coor)
        self.assertEqual(self.TestShip.getHits(),[Coor])
        self.TestShip.fire(Coor)
        self.assertEqual(self.TestShip.getHits(),[Coor])

    def testHasHits(self):
        Coor = Coordinate(4,1)
        self.assertFalse(self.TestShip.hasHit(Coor))
        self.TestShip.fire(Coor)
        self.assertTrue(self.TestShip.hasHit(Coor))

    def testIsSunk(self):
        for x in range(1,4):
            self.TestShip.fire(Coordinate(x,1))
            self.assertFalse(self.TestShip.isSunk())
        self.TestShip.fire(Coordinate(4,1))
        self.assertTrue(self.TestShip.isSunk())

    def testGetType(self):
        Type = self.TestShip.getType()
        self.assertIsInstance(Type,ShipType)
        self.assertEqual("HorizShip",Type.getName())

    def testGetCoordinates(self):
        assert_x_ys = [Coordinate(1,1),Coordinate(2,1),Coordinate(3,1),Coordinate(4,1)]
        x_ys = self.TestShip.getCoordinates()
        self.assertEqual(assert_x_ys,x_ys)

    def testIsConflict(self):
        Origin = Coordinate(1,0)
        Dir = VerticalDirection()
        Type = ShipType("VertShip",4)
        OtherShip = Ship(Type,Origin,Dir)
        self.assertTrue(self.TestShip.isConflict(OtherShip))

    def testIsNotConflict(self):
        Origin = Coordinate(0,0)
        Dir = VerticalDirection()
        Type = ShipType("VertShip",4)
        OtherShip = Ship(Type,Origin,Dir)
        self.assertFalse(self.TestShip.isConflict(OtherShip))

class TestVertShip(unittest.TestCase):
    def setUp(self):
        Origin = Coordinate(1,1)
        Dir = VerticalDirection()
        Type = ShipType("VertShip",4)
        self.TestShip = Ship(Type,Origin,Dir)

    def testIsHit(self):
        Coor = Coordinate(1,4)
        self.assertTrue(self.TestShip.isHit(Coor))

    def testIsNotHit(self):
        Coor = Coordinate(1,5)
        self.assertFalse(self.TestShip.isHit(Coor))

    def testShotAndHit(self):
        Coor = Coordinate(1,4)
        self.assertTrue(self.TestShip.fire(Coor))
        self.assertEqual(self.TestShip.getHits(),[Coor])

    def testShotAndMiss(self):
        Coor = Coordinate(1,5)
        self.assertFalse(self.TestShip.fire(Coor))
        self.assertEqual(self.TestShip.getHits(),[])

    def testGetHits(self):
        Coor = Coordinate(1,5)
        self.TestShip.fire(Coor)
        self.assertEqual(self.TestShip.getHits(),[])
        Coor1st = Coordinate(1,4)
        self.TestShip.fire(Coor1st)
        hits = self.TestShip.getHits()
        self.assertEqual(1,len(hits))
        Coor2nd = Coordinate(1,4)
        self.TestShip.fire(Coor2nd)
        hits = self.TestShip.getHits()
        self.assertEqual(1,len(hits))

    def testHasHits(self):
        Coor = Coordinate(1,4)
        self.assertFalse(self.TestShip.hasHit(Coor))
        self.TestShip.fire(Coor)
        self.assertTrue(self.TestShip.hasHit(Coor))

    def testIsSunk(self):
        for y in range(1,4):
            self.TestShip.fire(Coordinate(1,y))
            self.assertFalse(self.TestShip.isSunk())
        self.TestShip.fire(Coordinate(1,4))
        self.assertTrue(self.TestShip.isSunk())

    def testIsNotSunkIfSame(self):
        self.TestShip.fire(Coordinate(1,1))
        self.assertFalse(self.TestShip.isSunk())
        self.TestShip.fire(Coordinate(1,1))
        self.assertFalse(self.TestShip.isSunk())
        self.TestShip.fire(Coordinate(1,1))
        self.assertFalse(self.TestShip.isSunk())
        self.TestShip.fire(Coordinate(1,1))
        self.assertFalse(self.TestShip.isSunk())

    def testGetType(self):
        Type = self.TestShip.getType()
        self.assertIsInstance(Type,ShipType)
        self.assertEqual("VertShip",Type.getName())

    def testGetCoordinates(self):
        assert_x_ys = [Coordinate(1,1),Coordinate(1,2),Coordinate(1,3),Coordinate(1,4)]
        x_ys = self.TestShip.getCoordinates()
        self.assertEqual(assert_x_ys,x_ys)

    def testIsConflict(self):
        Origin = Coordinate(0,1)
        Dir = HorizontalDirection()
        Type = ShipType("HorizShip",4)
        OtherShip = Ship(Type,Origin,Dir)
        self.assertTrue(self.TestShip.isConflict(OtherShip))

    def testIsNotConflict(self):
        Origin = Coordinate(0,0)
        Dir = HorizontalDirection()
        Type = ShipType("HorizShip",4)
        OtherShip = Ship(Type,Origin,Dir)
        self.assertFalse(self.TestShip.isConflict(OtherShip))

