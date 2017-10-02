#!/usr/bin/env python3

# Use ``obxprop | grep _OB_APP`` to determine how to identify a particular 
# application.

from geometry import *
from xmlhelper import *

doc = make_document()
apps = make_root(doc, 'applications')

# Turn window decorations off for all applications.

app = make_element(doc, apps, 'application', **{'class':'*'})
make_text(doc, app, 'decor', 'no')

# Define initial positions for specific applications.

def place_app(doc, parent, name, x, y, w, h):
    app = make_element(doc, apps, 'application', name=name, type='normal')
    position = make_element(doc, app, 'position', force='yes')
    make_text(doc, position, 'x', x)
    make_text(doc, position, 'y', y)
    size = make_element(doc, app, 'size', force='yes')
    make_text(doc, size, 'width', w-6)
    make_text(doc, size, 'height', h-6)


place_app(doc, apps, 'sakura', 0, 0, left_width, top_height)
place_app(doc, apps, 'pithos', 0, 0, left_width, top_height)
place_app(doc, apps, 'gvim', 0, y, left_width, bottom_height + 30)
place_app(doc, apps, 'Navigator', x, 0, middle_right_width, full_height)

# Generate the applications file.

with open('sections/applications.xml', 'w') as file:
    doc.writexml(file, indent='  ', addindent='  ', newl='\n')
