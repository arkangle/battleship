
import unittest
from domain.ship import Ship
from domain.coordinate import Coordinate
from domain.direction import *
from domain.ship_type import *

class TestHorizShip(unittest.TestCase):
    def setUp(self):
        Origin = Coordinate((1,1))
        Dir = HorizontalDirection()
        Type = ShipType("HorizShip",4)
        self.TestShip = Ship(Type,Origin,Dir)

    def testIsHit(self):
        Coor = Coordinate((4,1))
        self.assertTrue(self.TestShip.isHit(Coor))

    def testIsNotHit(self):
        Coor = Coordinate((5,1))
        self.assertFalse(self.TestShip.isHit(Coor))

    def testShotAndHit(self):
        Coor = Coordinate((4,1))
        self.assertTrue(self.TestShip.shotAt(Coor))
        self.assertEquals(self.TestShip.getHits(),[Coor])

    def testShotAndMiss(self):
        Coor = Coordinate((5,1))
        self.assertFalse(self.TestShip.shotAt(Coor))
        self.assertEquals(self.TestShip.getHits(),[])

    def testGetHits(self):
        Coor = Coordinate((5,1))
        self.TestShip.shotAt(Coor)
        self.assertEquals(self.TestShip.getHits(),[])
        Coor = Coordinate((4,1))
        self.TestShip.shotAt(Coor)
        self.assertEquals(self.TestShip.getHits(),[Coor])
        self.TestShip.shotAt(Coor)
        self.assertEquals(self.TestShip.getHits(),[Coor])

    def testHasHits(self):
        Coor = Coordinate((4,1))
        self.assertFalse(self.TestShip.hasHit(Coor))
        self.TestShip.shotAt(Coor)
        self.assertTrue(self.TestShip.hasHit(Coor))

    def testIsSunk(self):
        for x in range(1,4):
            self.TestShip.shotAt(Coordinate((x,1)))
            self.assertFalse(self.TestShip.isSunk())
        self.TestShip.shotAt(Coordinate((x,1)))
        self.assertTrue(self.TestShip.isSunk())

    def testGetType(self):
        Type = self.TestShip.getType()
        self.assertIsInstance(Type,ShipType)
        self.assertEquals("HorizShip",Type.getName())

class TestVertShip(unittest.TestCase):
    def setUp(self):
        Origin = Coordinate((1,1))
        Dir = VerticalDirection()
        Type = ShipType("VertShip",4)
        self.TestShip = Ship(Type,Origin,Dir)

    def testIsHit(self):
        Coor = Coordinate((1,4))
        self.assertTrue(self.TestShip.isHit(Coor))

    def testIsNotHit(self):
        Coor = Coordinate((1,5))
        self.assertFalse(self.TestShip.isHit(Coor))

    def testShotAndHit(self):
        Coor = Coordinate((1,4))
        self.assertTrue(self.TestShip.shotAt(Coor))
        self.assertEquals(self.TestShip.getHits(),[Coor])

    def testShotAndMiss(self):
        Coor = Coordinate((1,5))
        self.assertFalse(self.TestShip.shotAt(Coor))
        self.assertEquals(self.TestShip.getHits(),[])

    def testGetHits(self):
        Coor = Coordinate((1,5))
        self.TestShip.shotAt(Coor)
        self.assertEquals(self.TestShip.getHits(),[])
        Coor = Coordinate((1,4))
        self.TestShip.shotAt(Coor)
        self.assertEquals(self.TestShip.getHits(),[Coor])
        self.TestShip.shotAt(Coor)
        self.assertEquals(self.TestShip.getHits(),[Coor])

    def testHasHits(self):
        Coor = Coordinate((1,4))
        self.assertFalse(self.TestShip.hasHit(Coor))
        self.TestShip.shotAt(Coor)
        self.assertTrue(self.TestShip.hasHit(Coor))

    def testIsSunk(self):
        for y in range(1,4):
            self.TestShip.shotAt(Coordinate((1,y)))
            self.assertFalse(self.TestShip.isSunk())
        self.TestShip.shotAt(Coordinate((1,y)))
        self.assertTrue(self.TestShip.isSunk())

    def testGetType(self):
        Type = self.TestShip.getType()
        self.assertIsInstance(Type,ShipType)
        self.assertEquals("VertShip",Type.getName())
