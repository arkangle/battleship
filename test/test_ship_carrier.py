
import unittest
from ship.carrier import Carrier

class TestCarrier(unittest.TestCase):
    def setUp(self):
        self.Ship = Carrier()
    def testShipLength(self):
        self.assertEquals(5,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Carrier",self.Ship.getName())
