from gi.repository import Gtk
import battle

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Battleship")
        self.set_border_width(10)
        self.set_default_size(340,180)
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Battleship"
        self.set_titlebar(header)

    def buildMain(self):
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        (player1_box,self.player1_entry) = self.buildEntryBox("Player 1")
        main_box.add(player1_box)
        (player2_box,self.player2_entry)= self.buildEntryBox("Player 2")
        main_box.add(player2_box)
        self.message_label = Gtk.Label("Enter Player Names")
        main_box.add(self.message_label)
        button = Gtk.Button("Start")
        button.connect("clicked",self.onStart)
        main_box.add(button)
        self.add(main_box)

    def buildEntryBox(self,description):
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        label = Gtk.Label(description)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Enter Name")
        box.add(label)
        box.add(entry)
        return (box,entry)

    def onStart(self,Button):
        if(self.player1_entry.get_text() == ""):
            self.message_label.set_text("Player 1 Name Required")
            self.player1_entry.grab_focus()
        elif(self.player2_entry.get_text() == ""):
            self.message_label.set_text("Player 2 Name Required")
            self.player2_entry.grab_focus()
        else:
            self.startBattle(self.player1_entry.get_text(),self.player2_entry.get_text())

    def startBattle(self,player1,player2):
        win = battle.Window(player1,player2)
        win.buildMain()
        win.connect("delete-event", self.returnWindow)
        win.show_all()
        self.hide()

    def returnWindow(self,window,arg):
        window.destroy()
        self.player1_entry.set_text("")
        self.player2_entry.set_text("")
        self.message_label.set_text("")
        self.show()
        self.player1_entry.grab_focus()
