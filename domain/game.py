
from domain.player import *
from domain.turn import *
from domain.battlefield import *

class Game:
    PlayerTurn = None
    @staticmethod
    def StartByName(name1,name2):
        Player1 = Player(name1,Battlefield())
        Player2 = Player(name2,Battlefield())
        turn = Turn(Player1,Player2)
        return Game(turn)

    def __init__(self,PlayerTurn):
        self.PlayerTurn = PlayerTurn

    def getPlayers(self):
        return self.PlayerTurn.getPlayers()

    def getPlayerByName(self,name):
        return self.PlayerTurn.getPlayerByName(name)
