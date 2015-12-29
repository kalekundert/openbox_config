#!/usr/bin/env python3

"""\
Determine where the division between the left and right panes should be based 
on the geometry of a window in the top left corner of the desktop.

Usage:
    ./geometry-from-screenshot.py

The bottom right coordinate of the top left window completely defines the 
layout of my openbox configuration, but determining this coordinate can be 
tedious.  This script determines it automatically.  Before running this script, 
position a window in the top left corner of the screen such that its bottom 
right corner is where you want it to be.  Make sure the window has a 3-pixel 
orange/grey border (from the "minimalist" theme), that the desktop is visible 
all around the window, and that the desktop is black.  The script works by 
taking a screenshot of the current desktop and looking for the transition 
between the orange/grey border and the black desktop, so the script will fail 
to correctly identify the window if any of the aforementioned conditions aren't 
met.  After running this script, run ``reconfigure.sh`` to update openbox.
"""

import json
import numpy as np

from sh import rm, scrot
from tempfile import mktemp
from matplotlib.image import imread
from pathlib import Path

try:
    screenshot_path = mktemp('.png')
    scrot(screenshot_path)
    rgb_pixels = imread(screenshot_path)
    black_pixels = np.max(rgb_pixels, axis=2) == 0
    division_width = np.nonzero(black_pixels[0,:])[0][0]
    division_height = np.nonzero(black_pixels[:,0])[0][0]
    geometry = int(division_width), int(division_height)

finally:
    rm(screenshot_path)

root_dir = Path(__file__).parent
geometry_json = root_dir / 'scripts' / 'geometry.json'

with geometry_json.open('w') as file:
    json.dump(geometry, file)


