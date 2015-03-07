from gi.repository import Gtk
import player_entry

win = player_entry.Window()
win.buildMain()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
