
import unittest
from domain.player import Player
from domain.turn import Turn
from domain.battlefield import Battlefield

class TestTurn(unittest.TestCase):
    def setUp(self):
        battlefield1 = Battlefield()
        battlefield2 = Battlefield()
        self.Player1 = Player("Player 1",battlefield1)
        self.Player2 = Player("Player 2",battlefield2)
        self.Turn = Turn(self.Player1,self.Player2)

    def testCurrentPlayer(self):
        Player = self.Turn.getCurrentPlayer()
        self.assertEqual(Player,self.Player1)

    def testOpponentPlayer(self):
        Player = self.Turn.getOpponentPlayer()
        self.assertEqual(Player,self.Player2)

    def testToggleBoolean(self):
        boolean = 0
        boolean = self.Turn.toggleBoolean(boolean)
        self.assertEqual(boolean,1)
        boolean = self.Turn.toggleBoolean(boolean)
        self.assertEqual(boolean,0)

    def testToggleTurn(self):
        self.Turn.toggleTurn()
        Player = self.Turn.getCurrentPlayer()
        self.assertEqual(Player,self.Player2)

    def testRandomTurn(self):
        track = 0
        for i in range(1,11):
            self.Turn.randomTurn()
            Player = self.Turn.getCurrentPlayer()
            if(Player == self.Player2):
                track += 1

        self.assertGreater(track,1)
        self.assertLess(track,9)

    def testGetPlayers(self):
        Players = self.Turn.getPlayers()
        self.assertEqual(Players[0],self.Player1)
        self.assertEqual(Players[1],self.Player2)
