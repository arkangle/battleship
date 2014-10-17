
import unittest
from ship.ship import Ship

class TestShip(unittest.TestCase):
    def setUp(self):
        self.Ship = Ship("TestShip",1)
    def testShipLength(self):
        self.assertEquals(1,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("TestShip",self.Ship.getName())
