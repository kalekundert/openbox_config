#!/usr/bin/env sh

# Query the connected monitors and decide which ones should be used.  
# Typically, only one monitor is used at a time.  If an external monitor is 
# present, it is preferred over the internal one.

INTERNAL=$(xrandr | grep LVDS | grep "\bconnected\b" | cut -d" " -f1)
EXTERNAL=$(xrandr | grep HDMI | grep "\bconnected\b" | cut -d" " -f1)

if [ -n "$EXTERNAL" ]; then
    xrandr --output $EXTERNAL --auto --output $INTERNAL --off

    # If something goes wrong, enable the internal monitor.
    if [ $? -ne 0 ]; then
        xrandr --output $INTERNAL --auto --output $EXTERNAL --off
        xbacklight -set 100
    fi
else
    xrandr --output $INTERNAL --auto --output HDMI1 --off --output HDMI2 --off
    xbacklight -set 100
fi

# Make the desktop black and replace caps lock with an extra control key.

xsetroot -solid black
setxkbmap -option ctrl:nocaps

# Recompiles the keybindings and updates the openbox configuration.  The path 
# to the configuration directory must be manually specified, although it is 
# usually ~/.config/openbox.

cd ~/.config/openbox

python scripts/keyboard.py
python scripts/compile.py

openbox --reconfigure
