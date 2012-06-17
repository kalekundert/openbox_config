# Note that this script is not executed if OpenBox is run as part of a GNOME
# session.

# Make the desktop background solid black.
xsetroot -solid black

# Replace the caps lock key with an additional control key.
xmodmap                                 \
    -e "remove Lock = Caps_Lock"        \
    -e "keysym Caps_Lock = Control_L"

