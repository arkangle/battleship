
import unittest
from domain.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.Player1 = Player("Player 1")
        self.Player2 = Player("Player 2")
    def testGetName(self):
        self.assertEquals(self.Player1.getName(),"Player 1")
        self.assertEquals(self.Player2.getName(),"Player 2")
