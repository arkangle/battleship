import cmd
from domain.game import Game

class Battleship(cmd.Cmd):
    prompt = "Battleship: "
    intro = "This is the classical game of battleship"
    Game = None
    def do_names(self,names):
        '''Supply two (2) Player Names'''
        if(names == None or len(names.split(" ")) < 2):
            name1 = input("Enter Player 1 Name: ")
            name2 = input("Enter Player 2 Name: ")
        else:
            named = names.split(" ")
            name1 = named[0]
            name2 = named[1]
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
        grid = self.Game.getGridPlayer(Player)
        rows = []
        rows.append(" " + "".join([str(c).rjust(3) for c in grid.getColumnLabels()]))
        for Row in grid.getRows():
            row = [Row.getLabel()]
            for Cell in Row.getCells():
                if Cell.isHit():
                    row.append("H")
                elif Cell.isMiss():
                    row.append("M")
                else:
                    row.append(".")
            rows.append("  ".join(row))
        print("\n".join(rows))
    def complete_battlefield(self, text, line, begidx, endidx):
        return self.completePlayerNames(text)
    def do_fire(self,args_str):
        '''Fire At Player'''
        args = args_str.split(" ")
        if(len(args) < 3):
            name = input("Player? ")
            row = input("Row (A-J)? ")
            column = input("Column (1-10)? ")
        else:
            name = args[0]
            row = args[1]
            column = args[2]
        try:
            row = row.upper()
            col = int(column)
            Player = self.Game.getPlayerByName(name)
            ship = self.Game.fireAtPlayer(Player,row,col)
            if(ship == None):
                print("Missed")
            elif ship.isSunk():
                print("The %s is Sunk!" % ship.getName())
            else:
                print("Hit")
        except ValueError:
            print("Invalid Coordinate")
    def completePlayerNames(self,text):
        completions = [Player.getName() for Player in self.Game.getPlayers() if Player.getName().startswith(text)]
        return completions
    def hasGame(self):
        return self.Game != None

if __name__ == '__main__' :
   Battleship().cmdloop() 
