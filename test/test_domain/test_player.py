
import unittest
from domain.player import Player
from domain.battlefield import Battlefield

class TestPlayer(unittest.TestCase):
    def setUp(self):
        battlefield1 = Battlefield()
        self.Player1 = Player("Player 1",battlefield1)

    def testGetName(self):
        self.assertEqual(self.Player1.getName(),"Player 1")

    def testGetBattlefield(self):
        self.assertIsInstance(self.Player1.getBattlefield(),Battlefield)
