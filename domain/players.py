import random
class Players:
    def __init__(self,Player1,Player2):
        self.players = [Player1,Player2]
        self.turn = 0

    def getCurrentPlayer(self):
        return self.players[self.turn]

    def toggleTurn(self):
        self.turn = 0 if self.turn == 1 else 1

    def randomTurn(self):
        self.turn = random.randrange(0,2)
