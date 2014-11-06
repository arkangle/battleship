import unittest
from domain.game import *

class TestGame(unittest.TestCase):
    def setUp(self):
        name1 = "Bob"
        name2 = "Sue"
        self.Game = Game.StartByName(name1,name2)
    def testStartByName(self):
        self.assertIsInstance(self.Game,Game)
    def testGetPlayers(self):
        Players = self.Game.getPlayers()
        self.assertEqual(Players[0].getName(),"Bob")
        self.assertEqual(Players[1].getName(),"Sue")
    def testGetPlayerByName(self):
        Bob = self.Game.getPlayerByName("Bob")
        self.assertEqual(Bob.getName(),"Bob")
        Sue = self.Game.getPlayerByName("Sue")
        self.assertEqual(Sue.getName(),"Sue")

