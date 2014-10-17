
import unittest
from ship.cruiser import Cruiser

class TestCruiser(unittest.TestCase):
    def setUp(self):
        self.Ship = Cruiser()
    def testShipLength(self):
        self.assertEquals(3,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Cruiser",self.Ship.getName())

