
import unittest
from domain.player import Player
from domain.players import Players

class TestPlayers(unittest.TestCase):
    def setUp(self):
        self.Player1 = Player("Player 1")
        self.Player2 = Player("Player 2")
        self.Players = Players(self.Player1,self.Player2)

    def testCurrentPlayer(self):
        Player = self.Players.getCurrentPlayer()
        self.assertEquals(Player,self.Player1)

    def testToggleTurn(self):
        self.Players.toggleTurn()
        Player = self.Players.getCurrentPlayer()
        self.assertEquals(Player,self.Player2)

    def testRandomTurn(self):
        track = 0
        for i in range(1,11):
            self.Players.randomTurn()
            Player = self.Players.getCurrentPlayer()
            if(Player == self.Player2):
                track += 1

        self.assertGreater(track,1)
        self.assertLess(track,9)
