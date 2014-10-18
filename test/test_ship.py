
import unittest
from domain.ship import *

class TestShip(unittest.TestCase):
    def setUp(self):
        self.Ship = Ship("TestShip",1)
    def testShipLength(self):
        self.assertEquals(1,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("TestShip",self.Ship.getName())

class TestBattleship(unittest.TestCase):
    def setUp(self):
        self.Ship = Battleship()
    def testShipLength(self):
        self.assertEquals(4,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Battleship",self.Ship.getName())

class TestCarrier(unittest.TestCase):
    def setUp(self):
        self.Ship = Carrier()
    def testShipLength(self):
        self.assertEquals(5,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Carrier",self.Ship.getName())

class TestCruiser(unittest.TestCase):
    def setUp(self):
        self.Ship = Cruiser()
    def testShipLength(self):
        self.assertEquals(3,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Cruiser",self.Ship.getName())

class TestDestroyer(unittest.TestCase):
    def setUp(self):
        self.Ship = Destroyer()
    def testShipLength(self):
        self.assertEquals(2,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Destroyer",self.Ship.getName())

class TestSubmarine(unittest.TestCase):
    def setUp(self):
        self.Ship = Submarine()
    def testShipLength(self):
        self.assertEquals(3,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Submarine",self.Ship.getName())
