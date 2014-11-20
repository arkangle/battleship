import cmd
from domain.game import Game
from domain.coordinate import Coordinate

class Battleship(cmd.Cmd):
    prompt = "Battleship: "
    intro = "This is the classical game of battleship"
    Game = None
    def do_names(self,empty):
        '''Supply two (2) Player Names'''
        name1 = input("Enter Player 1 Name: ")
        name2 = input("Enter Player 2 Name: ")
        self.Game = Game.StartByName(name1,name2)
    def do_players(self,empty):
        '''Print existing Players'''
        if not self.hasGame():
            self.do_names(None)
        Players = self.Game.getPlayers()
        print("Player 1: %s" % Players[0].getName())
        print("Player 2: %s" % Players[1].getName())
    def do_EOF(self,blank):
        '''Finish Well'''
        print("Bye For Now")
        return True
    def do_battlefield(self,name):
        '''Print Battlefield of Player'''
        Player = self.Game.getPlayerByName(name)
        Battlefield = Player.getBattlefield()
        Hits = Battlefield.getHits()
        Missed = Battlefield.getMissed()
        rows = []
        rows.append(" " + "".join([str(c).rjust(2) for c in Coordinate.columns]))
        for x in range(0,10):
            row = [Coordinate.rows[x]]
            for y in range(0,10):
                c = Coordinate((y,x))
                if Hits.count(c) > 0:
                    row.append("H")
                elif Missed.count(c) > 0:
                    row.append("M")
                else:
                    row.append(".")
            rows.append(" ".join(row))
        print("\n".join(rows))
    def complete_battlefield(self, text, line, begidx, endidx):
        return self.completePlayerNames(text)
    def do_fire(self,name):
        '''Fire At Other Player'''
        row = input("Row (A-J) ").upper()
        column = input("Column (1-10) ")
        try:
            c = Coordinate.Factory((row,int(column)))
            Player = self.Game.getPlayerByName(name)
            Battlefield = Player.getBattlefield()
            try:
                ship = Battlefield.shotAt(c)
                print("Hit")
            except ValueError:
                print("Missed")
        except ValueError:
            print("Invalid Coordinate {0},{1}" % (row,column))

    def complete_fire(self, text, line, begidx, endidx):
        return self.completePlayerNames(text)
    def completePlayerNames(self,text):
        completions = [Player.getName() for Player in self.Game.getPlayers() if Player.getName().startswith(text)]
        return completions
    def hasGame(self):
        return self.Game != None

if __name__ == '__main__' :
   Battleship().cmdloop() 
