
import unittest
from ship.submarine import Submarine

class TestSubmarine(unittest.TestCase):
    def setUp(self):
        self.Ship = Submarine()
    def testShipLength(self):
        self.assertEquals(3,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Submarine",self.Ship.getName())
