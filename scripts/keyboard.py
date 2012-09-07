#!/usr/bin/env python

# This script provides an expressive way to control openbox key-bindings.  The
# most prominent part of the script is the bindings dictionary, which maps
# hotkeys to actions.  Note that each hotkey is preceded by an implied 'Alt',
# or 'A-' in the language of openbox.

from bindings import *
from geometry import *

terminal = '/home/kale/hacking/installs/bin/sakura --geometry=%dx%d'
editor = '/home/kale/hacking/installs/bin/gvim'
browser = 'firefox'
ipython = terminal + ' --class=Python -e "zsh -ic ipython"'
openbox = '~/.config/openbox/reconfigure.sh'

bindings = {
        'q': Execute(terminal % short_terminal),
        'w': Execute(browser),
        'e': Execute(editor),
        'r': Execute(ipython % tall_terminal),

        'Up': Execute('amixer -q set Master 5%+ unmute'),
        'Down': Execute('amixer -q set Master 5%- unmute'),
        'S-Up': Execute('amixer -q set Master unmute'),
        'S-Down': Execute('amixer -q set Master mute'),
        'Left': Execute('/home/kale/hacking/scripts/music pause'),
        'Right': Execute('/home/kale/hacking/scripts/music skip'),

        'Escape': Execute(openbox),

        'a': GoToDesktop(1), 'C-a': SendToDesktop(1),
        's': GoToDesktop(2), 'C-s': SendToDesktop(2),
        'd': GoToDesktop(3), 'C-d': SendToDesktop(3),
        'f': GoToDesktop(4), 'C-f': SendToDesktop(4),
        'z': GoToDesktop(5), 'C-z': SendToDesktop(5),
        'x': GoToDesktop(6), 'C-x': SendToDesktop(6),
        'c': GoToDesktop(7), 'C-c': SendToDesktop(7),
        'v': GoToDesktop(8), 'C-v': SendToDesktop(8),

        'y': MoveResizeTo(0, 0, left_middle_width, full_height),
        'u': MoveResizeTo(0, 0, left_width, full_height),
        'i': MoveResizeTo(x, 0, middle_width, full_height),
        'o': MoveResizeTo(x, 0, middle_right_width, full_height),
        'p': MoveResizeTo(z, 0, right_width, full_height),

        'h': MoveResizeTo(0, 0, left_width, top_height),
        'j': MoveResizeTo(0, y, left_width, bottom_height),
        'k': MoveResizeTo(x, 0, middle_width, top_height),
        'l': MoveResizeTo(x, y, middle_width, bottom_height),

        'C-h': MoveResizeTo(0, 0, full_width, top_height),
        'C-j': MoveResizeTo(0, y, full_width, bottom_height),
        'C-k': MoveResizeTo(x, 0, middle_right_width, top_height),
        'C-r': MoveResizeTo(x, y, middle_right_width, bottom_height),

        'semicolon' : MoveResizeTo(z, 0, right_width, top_height),
        'apostrophe': MoveResizeTo(z, y, right_width, bottom_height),

        'n': Action('Iconify'),
        'm': Action('MaximizeFull'),

        'Tab': Action('NextWindow'),
        'S-Tab': Action('PreviousWindow'),
        'Return': GoToDesktop('last'),
        'S-Return': SendToDesktop('last'),

        'S-Escape': Action('Exit'), 
        'BackSpace': Action('Close') }

# XML Generation
keyboard = Keyboard()
keyboard.bind(**bindings)
keyboard.write('sections/keyboard.xml')

