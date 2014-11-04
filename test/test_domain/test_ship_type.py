
import unittest
from domain.ship_type import *

class TestShip(unittest.TestCase):
    def setUp(self):
        self.ShipType = ShipType("TestShip",1)
    def testShipLength(self):
        self.assertEqual(1,self.ShipType.getLength())
    def testShipName(self):
        self.assertEqual("TestShip",self.ShipType.getName())
    def testEquality(self):
        anotherShipType = ShipType("AnotherShip",1)
        closeShipType = ShipType("TestShip",3)
        sameShipType = ShipType("TestShip",1)
        self.assertNotEqual(self.ShipType,anotherShipType)
        self.assertNotEqual(self.ShipType,closeShipType)
        self.assertEqual(self.ShipType,sameShipType)

class TestBattleship(unittest.TestCase):
    def setUp(self):
        self.Ship = Battleship()
    def testShipLength(self):
        self.assertEqual(4,self.Ship.getLength())
    def testShipName(self):
        self.assertEqual("Battleship",self.Ship.getName())

class TestCarrier(unittest.TestCase):
    def setUp(self):
        self.Ship = Carrier()
    def testShipLength(self):
        self.assertEqual(5,self.Ship.getLength())
    def testShipName(self):
        self.assertEqual("Carrier",self.Ship.getName())

class TestCruiser(unittest.TestCase):
    def setUp(self):
        self.Ship = Cruiser()
    def testShipLength(self):
        self.assertEqual(3,self.Ship.getLength())
    def testShipName(self):
        self.assertEqual("Cruiser",self.Ship.getName())

class TestDestroyer(unittest.TestCase):
    def setUp(self):
        self.Ship = Destroyer()
    def testShipLength(self):
        self.assertEqual(2,self.Ship.getLength())
    def testShipName(self):
        self.assertEqual("Destroyer",self.Ship.getName())

class TestSubmarine(unittest.TestCase):
    def setUp(self):
        self.Ship = Submarine()
    def testShipLength(self):
        self.assertEqual(3,self.Ship.getLength())
    def testShipName(self):
        self.assertEqual("Submarine",self.Ship.getName())
