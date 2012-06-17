Installation
============
Copy these files into the openbox configuration directory, which usually has
the following path:

    ~/.config/openbox

By default, the configuration files use PyGTK to determine how large the screen
is and to adjust the size of the windows accordingly.  On Red Hat systems,
these libraries can be installed using the following command:

    $ yum install pygtk2

Alternatively, the size of the screen can be specified manually be setting the
screen_width and screen_height parameters in the scripts/geometry.py script.

The following command can be used to force OpenBox to load the new
configuration files:

    $ openbox --reconfigure

Many of the keybindings use the control key.  This is much more convenient if
the caps lock key is replaced with an extra control.  This can be done without
too much trouble in GNOME, but I won't outline the process here because the
internet is probably more up to date.

Keybindings for Launching Programs
==================================
These keybindings may need to be customized to your system, because everyone
likes to use different editors and browsers.  You can specify your favorite
programs in the main keybinding script:

    ~/.config/openbox/scripts/keyboard.py

For the terminal specifically, I've removed both the menu and the scrollbars.
This helps the window fit better when using the default window sizes.

A-q             Launch a terminal.          (Default: gnome-terminal)
A-w             Launch a web browser.       (Default: firefox)
A-e             Launch a python shell.      (Default: ipython)
A-r             Launch a root login shell.
A-C-q           Launch a text editor.       (Default: gvim)

A-Backspace     Close the currently active window.
A-S-Escape      Rerun the openbox configuration script.
A-Escape        Log out of the system.

Keybindings for Switching Focus
===============================
A-Tab           Cycle through the active windows in the usual order.
A-C-Tab         Cycle through the active windows in reverse order.

A-a             Switch to desktop #1.
A-s             Switch to desktop #2.
A-d             Switch to desktop #3.
A-f             Switch to desktop #4.
A-z             Switch to desktop #5.
A-x             Switch to desktop #6.
A-c             Switch to desktop #7.
A-v             Switch to desktop #8.

A-Return        Switch to the previously active desktop.

Keybindings for Resizing Windows
================================
Most of these commands behave as if the screen is divided into a grid with
three columns and two rows.  The left and middle columns are the same size, but
the relative size right column really depends on the screen dimensions.  The
top row is smaller than the bottom one.

A-h             Move to the top-left position.
A-j             Move to the bottom-left position.
A-k             Move to the top-middle position.
A-l             Move to the bottom-middle position.
A-;             Move to the top-right position.
A-'             Move to the bottom-right position.

A-y             Fill the left and middle columns.
A-u             Fill the left column.
A-i             Fill the middle column.
A-o             Fill the middle and right columns.
A-p             Fill the right column.

A-C-h           Fill the top row.
A-C-j           Fill the bottom row.
A-C-k           Fill the top row, starting from the middle column.
A-C-l           Fill the bottom row, starting from the middle column.

A-n             Minimize the current window.
A-m             Maximize the current window.

A-C-a           Move to desktop #1.
A-C-s           Move to desktop #2.
A-C-d           Move to desktop #3.
A-C-f           Move to desktop #4.
A-C-z           Move to desktop #5.
A-C-x           Move to desktop #6.
A-C-c           Move to desktop #7.
A-C-v           Move to desktop #8.

A-C-Return      Move to the previously active desktop.

