#!/usr/bin/env sh

# This script recompiles the keybindings and updates the openbox configuration.
# The path to the configuration directory must be manually specified, although
# it is usually ~/.config/openbox.

cd ~/.config/openbox

python scripts/keyboard.py
python scripts/compile.py

openbox --reconfigure
