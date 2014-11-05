import cmd
from domain.game import Game

class Battleship(cmd.Cmd):
    prompt = "Battleship: "
    intro = "This is the classical game of battleship"
    Game = None
    def do_names(self,empty):
        '''Supply two (2) Player Names'''
        name1 = input("Enter Player 1 Name: ")
        name2 = input("Enter Player 2 Name: ")
        self.Game = Game.StartByName(name1,name2)
    def hasGame(self):
        return self.Game != None
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
        pass
    def complete_battlefield(self, text, line, begidx, endidx):
        Players = self.Game.getPlayers()
        names = [Players[0].getName(),Players[1].getName()]
        if not text:
            completions = names
        else:
            completions = []
            for name in names:
                if name.startswith(text):
                    completions.append(name)
        return completions

if __name__ == '__main__' :
   Battleship().cmdloop() 
