
import unittest
from ship.battleship import Battleship

class TestBattleship(unittest.TestCase):
    def setUp(self):
        self.Ship = Battleship()
    def testShipLength(self):
        self.assertEquals(4,self.Ship.getLength())
    def testShipName(self):
        self.assertEquals("Battleship",self.Ship.getName())
