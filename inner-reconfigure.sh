#!/usr/bin/env sh

set -x
date

# Make the desktop black and replace caps lock with an extra control key.

xsetroot -solid black
setxkbmap -option ctrl:nocaps -option altwin:swap_alt_win

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

INTERNAL=$(xrandr | grep 'LVDS' | grep "\bconnected\b" | cut -d" " -f1)
EXTERNAL=$(xrandr | grep 'HDMI\|VGA\|DP' | grep "\bconnected\b" | cut -d" " -f1)

if [ -n "$EXTERNAL" ]; then
    xrandr --output $EXTERNAL --off --output $INTERNAL --off
    xrandr --output $EXTERNAL --auto

    # If something goes wrong, enable the internal monitor.
    if [ $? -ne 0 ]; then
        xrandr --output $INTERNAL --auto --output $EXTERNAL --off
    fi
else
    xrandr --output $INTERNAL --auto --output HDMI1 --off --output HDMI2 --off
fi

# Recompiles the keybindings and updates the openbox configuration.  The path 
# to the configuration directory must be manually specified, although it is 
# usually ~/.config/openbox.

cd ~/.config/openbox

python2 scripts/keyboard.py
python2 scripts/compile.py

openbox --reconfigure
