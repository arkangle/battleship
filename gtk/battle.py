from gi.repository import Gtk
from domain.game import Game
import string

class Window(Gtk.Window):
    def __init__(self,player1,player2):
        Gtk.Window.__init__(self, title="Battleship")
        self.set_border_width(10)
        self.set_default_size(540,480)
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Battleship"
        self.set_titlebar(header)
        self.setupGame(player1,player2)

    def setupGame(self,player1,player2):
        self.game = Game.StartByName(player1,player2)
        self.game.getPlayerTurn().randomTurn()
        players = self.game.getPlayers()
        self.game.randomPlacementsPlayer(players[0])
        self.game.randomPlacementsPlayer(players[1])

    def buildPlayerBox(self):
        players = self.game.getPlayers()
        players_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        player1_label = Gtk.Label("Player 1: %s" % players[0].getName())
        players_box.pack_start(player1_label,True,True,0)
        player2_label = Gtk.Label("Player 2: %s" % players[1].getName())
        players_box.pack_end(player2_label,True,True,0)
        return players_box

    def buildMain(self):

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        players_box = self.buildPlayerBox()    
        main_box.add(players_box)

        self.action_label = Gtk.Label("Start Game")
        main_box.add(self.action_label)
        
        OpponentGameGrid = self.game.getGridPlayer(self.game.getPlayerTurn().getOpponentPlayer())
        grid = self.buildFireGrid(OpponentGameGrid)
        main_box.add(grid)
        self.add(main_box)

    def buildFireGrid(self,GameGrid):
        grid = Gtk.Grid()
        grid.set_column_spacing(2)
        grid.set_row_spacing(2)
        grid.set_halign(Gtk.Align.CENTER)
        grid.attach(Gtk.Label(""),0,0,1,1)
        x = 1
        for c in GameGrid.getColumnLabels():
            grid.attach(Gtk.Label(c),x,0,1,1)
            x += 1
        y = 1
        for Row in GameGrid.getRows():
            grid.attach(Gtk.Label(Row.getLabel()),0,y,1,1)
            x = 1
            for Cell in Row.getCells():
                coordinate = self.game.getCoordinate(x-1,y-1)
                button = Button(coordinate,Cell)
                button.connect("clicked",self.onFireAction)
                grid.attach(button,x,y,1,1)
                x += 1
            y += 1
        return grid


    def onFireAction(self,Button):
        coordinate = Button.getCoordinate()
        if(Button.isGuessed()):
            txt = "You Fired at: (%s,%s) but is already %s!" % (coordinate.getRow(),coordinate.getColumn(),Button.get_label())
            self.action_label.set_label(txt)
        else:
            Player = self.game.getPlayerTurn().getCurrentPlayer()
            Opponent = self.game.getPlayerTurn().getOpponentPlayer()
            ship = self.game.fireAtPlayer(Opponent,coordinate.getRow(),coordinate.getColumn())
            if(ship == None):
                txt = "%s Fired at: (%s,%s) and was a Miss!" % (Player.getName(),coordinate.getRow(),coordinate.getColumn())
            else:
                if ship.isSunk():
                    txt = "%s Fired at: (%s,%s) " % (Player.getName(),coordinate.getRow(),coordinate.getColumn())
                    txt = txt + "and sunk %s's %s" % (Opponent.getName(),ship.getType().getName())
                    if(self.game.didLosePlayer(Opponent)):
                        txt = txt + " and won!"
                else:
                    txt = "%s Fired at: (%s,%s) and was a Hit!" % (Player.getName(),coordinate.getRow(),coordinate.getColumn())
            self.action_label.set_label(txt)
            Button.shot()
            Button.setStatus()

class Button(Gtk.Button):
    def __init__(self,coordinate,cell):
        Gtk.Button.__init__(self)
        self.coordinate = coordinate
        self.cell = cell
        self.setStatus()

    def getCoordinate(self):
        return self.coordinate

    def setStatus(self):
        if self.cell.isHit():
            self.set_label("Hit")
            self.set_relief(Gtk.ReliefStyle.NONE)
        elif self.cell.isMiss():
            self.set_label("Miss")
            self.set_relief(Gtk.ReliefStyle.NONE)
        else:
            self.set_label("????")

    def shot(self):
        self.cell.shot()

    def isGuessed(self):
        return self.cell.isHit() or self.cell.isMiss()
