from domain.player import *
from domain.turn import *
from domain.battlefield import *
from domain.coordinate import *
from domain.grid import *
from domain.direction import *
from domain.ship import *
from domain.ship_type import *
import random
import sys

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

    def createCoordinate(self,row,column):
        C = Coordinate.Factory(row,int(column))
        return C

    def fireAtPlayer(self,player,row,column):
        C = self.createCoordinate(row,column)
        Battlefield = player.getBattlefield()
        return Battlefield.fire(C)

    def didLosePlayer(self,player):
        Battlefield = player.getBattlefield()
        return Battlefield.areAllSunk()

    def getGridPlayer(self,player):
        Battlefield = player.getBattlefield()
        return Grid.factory(Battlefield.Missed,Battlefield.ShipCollection)

    def randomPlacementsPlayer(self,player):
        Battlefield = player.getBattlefield()
        ShipTypes = [Battleship(),Carrier(),Cruiser(),Destroyer(),Submarine()]
        Directions = [HorizontalDirection(),VerticalDirection()]
        for ship_type in ShipTypes:
            retry = True
            while(retry):
                rand_dir = random.randrange(0,2)
                rand_x = random.randrange(0,10)
                rand_y = random.randrange(0,10)
                rand_Coordinate = Coordinate(rand_x,rand_y)
                rand_Direction = Directions[rand_dir]
                rand_Ship = Ship(ship_type,rand_Coordinate,rand_Direction)
                try:
                    Battlefield.addShip(rand_Ship)
                    retry = False
                except:
                    pass
