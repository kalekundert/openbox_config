#!/usr/bin/env python3

import subprocess, json, pathlib

onyx = { "top" : 22, "bottom" : 2, "sides" : 2 }
clearlooks  = { "top" : 20, "bottom" : 5, "sides" : 2 }
minimalist = { "top" : 3, "bottom" : 3, "sides" : 3 }
theme = minimalist
vertical_padding = theme["top"] + theme["bottom"]
horizontal_padding = 2 * theme["sides"]

# This module defines the geometry of every window assigned to a key binding.
# The four most important parameters are screen_width, screen_height,
# division_width, and division_height.  The rest of the parameters are derived
# from these four.
#
# The screen dimensions are grabbed from GTK.  If the python bindings to GTK
# are not installed, the resolution of the screen can be specified manually.
# The division width and height define the dimensions of the grid that the
# windows fit into.  The default parameters were chosen to fit well with
# 80-character terminals using a 10-point monospace font.

xrandr = subprocess.check_output('xrandr').decode()
for line in xrandr.split('\n'):
    if '*' in line:
        resolution = line.split()[0].split('x')
        screen_width = int(resolution[0])
        screen_height = int(resolution[1])

# When using a 10-point monospace font, each column in a gvim window is 8
# pixels wide.  The full width of the window is 10 pixels wider than the sum of
# the columns to account for 5 pixels of padding on each side of the window.
# 3 of these pixels are provided by the window manager and should be taken from
# the theme definition.  The 2 remaining pixels are provided by gvim and cannot
# be changed.

scripts_dir = pathlib.Path(__file__).parent
geometry_json = scripts_dir / 'geometry.json'

if not geometry_json.is_file():
    rows, columns = 24, 80 if screen_width >= 1600 else 72
    division_width = 8 * columns + 4 + horizontal_padding
    division_height = 15 * rows + 5 + vertical_padding

with geometry_json.open() as file:
    division_width, division_height = json.load(file)

x = division_width
y = division_height
xx = 2 * division_width
x12 = screen_width // 2
x13 = screen_width // 3
x23 = 2 * screen_width // 3

full_width = screen_width
full_height = screen_height

left_width = division_width
left_middle_width = 2 * division_width
middle_width = left_width
middle_right_width = full_width - division_width
right_width = middle_right_width - division_width
half_width = screen_width // 2
third_width = screen_width // 3

top_height = division_height
bottom_height = full_height - division_height

short_terminal = (
        left_width - horizontal_padding - 2,
        top_height - vertical_padding - 2)

tall_terminal = (
        left_width - horizontal_padding - 2,
        bottom_height - vertical_padding - 2)

