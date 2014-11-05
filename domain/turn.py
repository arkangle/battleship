import random

class Turn:
    def __init__(self,Player1,Player2):
        self.players = [Player1,Player2]
        self.turn = 0

    def getCurrentPlayer(self):
        return self.players[self.turn]

    def getOpponentPlayer(self):
        opponent = self.toggleBoolean(self.turn)
        return self.players[opponent]

    def getPlayers(self):
        return self.players

    def toggleTurn(self):
        self.turn = self.toggleBoolean(self.turn)

    def toggleBoolean(self,number):
        return 0 if number == 1 else 1

    def randomTurn(self):
        self.turn = random.randrange(0,2)
