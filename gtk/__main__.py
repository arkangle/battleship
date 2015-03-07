from gi.repository import Gtk
import gtk.player_entry

win = gtk.player_entry.Window()
win.buildMain()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
