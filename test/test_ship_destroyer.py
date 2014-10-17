
import unittest
from ship.destroyer import Destroyer

class TestDestroyer(unittest.TestCase):
    def setUp(self):
        self.Ship = Destroyer()
    def testShipLength(self):
        self.assertEquals(2,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Destroyer",self.Ship.getName())

