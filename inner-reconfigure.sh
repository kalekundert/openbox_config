#!/usr/bin/env sh

set -x
date

# Make the desktop black and replace caps lock with an extra control key.

xsetroot -solid black
setxkbmap -option ctrl:nocaps -option altwin:swap_alt_win -option compose:rctrl -option terminate:ctrl_alt_bksp

# Disable screen blanking.  Use `set dpms force off` to blank the screen
# manually.  See the Arch Wiki:
# https://wiki.archlinux.org/title/Display_Power_Management_Signaling

xset s off -dpms

# Turn off beeping (don't know how this got enabled in the first place).

xset b off

# Configure middle-mouse scrolling.

function configure_trackpoint () {
    xinput set-prop "$1" "Evdev Wheel Emulation" 1
    xinput set-prop "$1" "Evdev Wheel Emulation Button" 2
    xinput set-prop "$1" "Evdev Wheel Emulation Timeout" 200
    xinput set-prop "$1" "Evdev Wheel Emulation Axes" 6 7 4 5
}

configure_trackpoint "TPPS/2 IBM TrackPoint"
configure_trackpoint "pointer:Lite-On Technology Corp. ThinkPad USB Keyboard with TrackPoint"

# Query the connected monitors and decide which ones should be used.  
# Typically, only one monitor is used at a time.  If an external monitor is 
# present, it is preferred over the internal one.

# 2022/08/01: After an OS update, this command became necessary.  Without it, 
# any xrandr command fails with the following error:
#
# xrandr: output LVDS1 cannot use rotation "normal" reflection "none"
xrandr --output LVDS1 --rotate normal --reflect normal
python3 pick-monitors.py

# Recompiles the keybindings and updates the openbox configuration.  The path 
# to the configuration directory must be manually specified, although it is 
# usually ~/.config/openbox.

cd ~/.config/openbox

python3 scripts/keyboard.py
python3 scripts/applications.py
python3 scripts/compile.py

openbox --reconfigure
