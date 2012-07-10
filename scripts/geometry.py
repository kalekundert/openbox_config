import gtk

# This module defines the geometry of every window assigned to a keybinding.
# The four most important parameters are screen_width, screen_height,
# division_width, and division_height.  The rest of the parameters are derived
# from these four.
#
# The screen dimensions are grabbed from GTK.  If the python bindings to GTK
# are not installed, the resolution of the screen can be specified manually.
# The division width and height define the dimensions of the grid that the
# windows fit into.  The default parameters were chosen to fit well with
# 80-character terminals using a 10-point monospace font.

screen_width = gtk.gdk.screen_width()
screen_height = gtk.gdk.screen_height()

x = division_width = 650 if screen_height > 1600 else 586
y = division_height = 386
z = 2 * division_width

onyx = { "top" : 22, "bottom" : 2, "sides" : 2 }
clearlooks  = { "top" : 20, "bottom" : 5, "sides" : 2 }
minimalist = { "top" : 3, "bottom" : 3, "sides" : 3 }

vertical_padding = minimalist["top"] + minimalist["bottom"]
horizontal_padding = 2 * minimalist["sides"]

full_width = screen_width - horizontal_padding
full_height = screen_height - vertical_padding

left_width = division_width - horizontal_padding
left_middle_width = 2 * division_width - horizontal_padding
middle_width = left_width
middle_right_width = full_width - division_width
right_width = middle_right_width - division_width

top_height = division_height - vertical_padding
bottom_height = full_height - division_height

short_terminal = left_width - 2, top_height - 2
tall_terminal = left_width - 2, bottom_height - 2

