#!/usr/bin/env python

# This script provides an expressive way to control openbox key-bindings.  The
# most prominent part of the script is the bindings dictionary, which maps
# hotkeys to actions.  You can find the name for any key-press by running the 
# 'xev' command.

from bindings import *
from geometry import *

terminal = 'sakura'
python = 'sakura -x xonsh'
browser = 'qutebrowser'
email = 'thunderbird'
editor = 'gvim'
runner = 'gmrun'
openbox = '~/.config/openbox/reconfigure.sh'
backlight = 'xbacklight -steps 1 -%s 5'
audio = 'pulseaudio-ctl %s'
display = 'arandr'
sleep = 'systemctl suspend'

bindings = {
        'A-Escape': Execute(openbox),
        'W-Escape': Execute(openbox),
        'W-C-S-Escape': Execute(openbox + ' --debug'),

        'W-q': Execute(terminal),
        'W-C-Q': Execute(python),
        'W-w': Execute(browser),
        'W-C-w': Execute(email),
        'W-e': Execute(editor),
        'W-r': Execute(runner),

        'XF86Sleep': Execute(sleep),
        'XF86Display': Execute(display),
        'XF86AudioMute': Execute(audio % 'mute'),
        'XF86AudioLowerVolume': Execute(audio % 'down 5'),
        'XF86AudioRaiseVolume': Execute(audio % 'up 5'),
        'XF86MonBrightnessUp': Execute(backlight % 'inc'),
        'XF86MonBrightnessDown': Execute(backlight % 'dec'),

        'W-a': GoToDesktop(1), 'W-C-a': SendToDesktop(1),
        'W-s': GoToDesktop(2), 'W-C-s': SendToDesktop(2),
        'W-d': GoToDesktop(3), 'W-C-d': SendToDesktop(3),
        'W-f': GoToDesktop(4), 'W-C-f': SendToDesktop(4),
        'W-z': GoToDesktop(5), 'W-C-z': SendToDesktop(5),
        'W-x': GoToDesktop(6), 'W-C-x': SendToDesktop(6),
        'W-c': GoToDesktop(7), 'W-C-c': SendToDesktop(7),
        'W-v': GoToDesktop(8), 'W-C-v': SendToDesktop(8),
        'W-S-a': GoToDesktop(9), 'W-C-S-a': SendToDesktop(9),
        'W-S-s': GoToDesktop(10), 'W-C-S-s': SendToDesktop(10),
        'W-S-d': GoToDesktop(11), 'W-C-S-d': SendToDesktop(11),
        'W-S-f': GoToDesktop(12), 'W-C-S-f': SendToDesktop(12),
        'W-S-z': GoToDesktop(13), 'W-C-S-z': SendToDesktop(13),
        'W-S-x': GoToDesktop(14), 'W-C-S-x': SendToDesktop(14),
        'W-S-c': GoToDesktop(15), 'W-C-S-c': SendToDesktop(15),
        'W-S-v': GoToDesktop(16), 'W-C-S-v': SendToDesktop(16),

        'W-y': MoveResizeTo(0, 0, left_middle_width, full_height),
        'W-u': MoveResizeTo(0, 0, left_width, full_height),
        'W-i': MoveResizeTo(x, 0, middle_width, full_height),
        'W-o': MoveResizeTo(x, 0, middle_right_width, full_height),
        'W-p': MoveResizeTo(z, 0, right_width, full_height),

        'W-h': MoveResizeTo(0, 0, left_width, top_height),
        'W-j': MoveResizeTo(0, y, left_width, bottom_height),
        'W-k': MoveResizeTo(x, 0, middle_width, top_height),
        'W-l': MoveResizeTo(x, y, middle_width, bottom_height),

        'W-S-h': MoveTo(0, 0),
        'W-S-j': MoveTo(0, y),
        'W-S-k': MoveTo(x, 0),
        'W-S-l': MoveTo(x, y),

        'W-C-h': MoveResizeTo(0, 0, full_width, top_height),
        'W-C-j': MoveResizeTo(0, y, full_width, bottom_height),
        'W-C-k': MoveResizeTo(x, 0, middle_right_width, top_height),
        'W-C-l': MoveResizeTo(x, y, middle_right_width, bottom_height),

        'W-semicolon': MoveResizeTo(z, 0, right_width, top_height),
        'W-apostrophe': MoveResizeTo(z, y, right_width, bottom_height),
        'W-bracketleft': MoveResizeTo(0, 0, half_width, full_height),
        'W-bracketright': MoveResizeTo(q, 0, half_width, full_height),

        'W-n': Action('Iconify'),
        'W-m': MoveResizeTo(0, 0, full_width, full_height),

        'W-Tab': Action('NextWindow'),
        'W-S-Tab': Action('PreviousWindow'),
        'W-C-Tab': Action('PreviousWindow'),
        'W-Return': GoToDesktop('last'),
        'W-S-Return': SendToDesktop('last'),

        'W-S-Escape': Action('Exit'), 
        'W-BackSpace': Action('Close') }

# XML Generation
keyboard = Keyboard()
keyboard.bind(**bindings)
keyboard.write('sections/keyboard.xml')

