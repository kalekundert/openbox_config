#!/usr/bin/env python

# This script provides an expressive way to control openbox key-bindings.  The
# most prominent part of the script is the bindings dictionary, which maps
# hotkeys to actions.  Note that each hotkey is preceded by an implied 'Alt',
# or 'A-' in the language of openbox.  You can find the name for any other key 
# by running the 'xev' command.

from bindings import *
from geometry import *

terminal = '/home/kale/hacking/installs/bin/sakura --geometry=%dx%d'
editor = 'gvim'
browser = 'firefox'
email = 'thunderbird'
ipython = terminal + ' --class=Python -e "zsh -ic ipython"'
openbox = '~/.config/openbox/reconfigure.sh'
pianobar = '/home/kale/hacking/scripts/music %s'

bindings = {
        'q': Execute(terminal % short_terminal),
        'w': Execute(browser),
        'C-w': Execute(email),
        'e': Execute(editor),
        'r': Execute(ipython % tall_terminal),

        'Up': Execute(pianobar % 'louder'),
        'Down': Execute(pianobar % 'quieter'),
        'S-Up': Execute(pianobar % 'unmute'),
        'S-Down': Execute(pianobar % 'mute'),
        'Left': Execute(pianobar % 'pause'),
        'Right': Execute(pianobar % 'skip'),
        'S-Left': Execute(pianobar % 'love'),
        'S-Right': Execute(pianobar % 'hate'),

        'Escape': Execute(openbox),

        'a': GoToDesktop(1), 'C-a': SendToDesktop(1),
        's': GoToDesktop(2), 'C-s': SendToDesktop(2),
        'd': GoToDesktop(3), 'C-d': SendToDesktop(3),
        'f': GoToDesktop(4), 'C-f': SendToDesktop(4),
        'z': GoToDesktop(5), 'C-z': SendToDesktop(5),
        'x': GoToDesktop(6), 'C-x': SendToDesktop(6),
        'c': GoToDesktop(7), 'C-c': SendToDesktop(7),
        'v': GoToDesktop(8), 'C-v': SendToDesktop(8),
        'S-a': GoToDesktop(9), 'C-S-a': SendToDesktop(9),
        'S-s': GoToDesktop(10), 'C-S-s': SendToDesktop(10),
        'S-d': GoToDesktop(11), 'C-S-d': SendToDesktop(11),
        'S-f': GoToDesktop(12), 'C-S-f': SendToDesktop(12),
        'S-z': GoToDesktop(13), 'C-S-z': SendToDesktop(13),
        'S-x': GoToDesktop(14), 'C-S-x': SendToDesktop(14),
        'S-c': GoToDesktop(15), 'C-S-c': SendToDesktop(15),
        'S-v': GoToDesktop(16), 'C-S-v': SendToDesktop(16),

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
        'C-l': MoveResizeTo(x, y, middle_right_width, bottom_height),

        'semicolon': MoveResizeTo(z, 0, right_width, top_height),
        'apostrophe': MoveResizeTo(z, y, right_width, bottom_height),
        'bracketleft': MoveResizeTo(0, 0, half_width, full_height),
        'bracketright': MoveResizeTo(q, 0, half_width, full_height),

        'n': Action('Iconify'),
        'm': MoveResizeTo(0, 0, full_width, full_height),

        'Tab': Action('NextWindow'),
        'S-Tab': Action('PreviousWindow'),
        'C-Tab': Action('PreviousWindow'),
        'Return': GoToDesktop('last'),
        'S-Return': SendToDesktop('last'),

        'S-Escape': Action('Exit'), 
        'BackSpace': Action('Close') }

# XML Generation
keyboard = Keyboard()
keyboard.bind(**bindings)
keyboard.write('sections/keyboard.xml')

