from gi.repository import Gtk
import gui.player_entry

win = gui.player_entry.Window()
win.buildMain()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
