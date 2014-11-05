import cmd
from domain.game import Game

class Battleship(cmd.Cmd):
    prompt = "Battleship: "
    intro = "This is the classical game of battleship"
    Game = None
    def do_names(self,names):
        '''Supply two (2) Player Names'''
        named = names.split()
        if(len(named) == 2):
            self.Game = Game.StartByName(named[0],named[1])
        else:
            print("Two (2) Player Names Required")
    def hasGame(self):
        return self.Game != None
    def do_players(self,empty):
        '''Print existing Players'''
        if not self.hasGame():
            print("Game Not Created Yet")
        else:
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
