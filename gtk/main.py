from gi.repository import Gtk
import string
import random

class BattleshipWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Battleship")
        self.set_border_width(10)
        self.set_default_size(640,480)
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Battleship"
        self.set_titlebar(header)

    def buildScreen(self):
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(main_box)

        player1_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        main_box.add(player1_box)
        player1_label = Gtk.Label("Player 1 Name")
        player1_entry = Gtk.Entry()
        player1_box.add(player1_label)
        player1_box.add(player1_entry)

        player2_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        main_box.add(player2_box)
        player2_label = Gtk.Label("Player 2 Name")
        player2_entry = Gtk.Entry()
        player2_box.add(player2_label)
        player2_box.add(player2_entry)

        self.action_label = Gtk.Label("Actions Go Here")
        main_box.add(self.action_label)

        grid = Gtk.Grid()
        grid.set_column_spacing(2)
        grid.set_row_spacing(2)
        grid.attach(Gtk.Label(""),0,0,1,1)
        for x in range(1,11):
            grid.attach(Gtk.Label(x),x,0,1,1)
        for y in range(1,11):
            grid.attach(Gtk.Label(string.ascii_uppercase[y-1]),0,y,1,1)
        for y in range(1,11):
            for x in range(1,11):
                button = BattleshipButton(y,x)
                button.connect("clicked",self.onFireAction)
                grid.attach(button,x,y,1,1)
        main_box.add(grid)

    def onFireAction(self,Button):
        location = Button.getLocation()
        if(Button.isGuessed()):
            txt = "You Fired at: (%s,%s) but is already %s!" % (string.ascii_uppercase[location[0]-1],location[1],Button.get_label())
            self.action_label.set_label(txt)
        else:
            status = random.choice(("H","M"))
            Button.setStatus(status)
            txt = "You Fired at: (%s,%s) and was a %s!" % (string.ascii_uppercase[location[0]-1],location[1],Button.get_label())
            self.action_label.set_label(txt)


class BattleshipButton(Gtk.Button):
    def __init__(self,y,x):
        Gtk.Button.__init__(self)
        self.y = y
        self.x = x
        self.setStatus("?")

    def getLocation(self):
        return (self.y,self.x)

    def setStatus(self,status):
        self.hit_status = status
        if(status == "?"):
            self.set_label("????")
        elif(status == "H"):
            self.set_label("Hit")
            self.set_relief(Gtk.ReliefStyle.NONE)
        elif(status == "M"):
            self.set_label("Miss")
            self.set_relief(Gtk.ReliefStyle.NONE)
    def isGuessed(self):
        return self.hit_status != "?"


win = BattleshipWindow()
win.buildScreen()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
