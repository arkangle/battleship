
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

    def testGetEndXY(self):
        end_x_y = self.TestShip.getEndXY()
        self.assertEquals((5,1),end_x_y)

    def testIsHit(self):
        Coor = Coordinate((4,1))
        self.assertTrue(self.TestShip.isHit(Coor))

    def testIsNotHit(self):
        Coor = Coordinate((5,1))
        self.assertFalse(self.TestShip.isHit(Coor))

class TestVertShip(unittest.TestCase):
    def setUp(self):
        Origin = Coordinate((1,1))
        Dir = VerticalDirection()
        Type = ShipType("VertShip",4)
        self.TestShip = Ship(Type,Origin,Dir)

    def testGetEndXY(self):
        end_x_y = self.TestShip.getEndXY()
        self.assertEquals((1,5),end_x_y)

    def testIsHit(self):
        Coor = Coordinate((1,4))
        self.assertTrue(self.TestShip.isHit(Coor))

    def testIsNotHit(self):
        Coor = Coordinate((1,5))
        self.assertFalse(self.TestShip.isHit(Coor))
