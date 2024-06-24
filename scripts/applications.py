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

def place_app(doc, parent, id, x, y, w, h, desktop=None):
    if isinstance(id, str):
        id = {'name': id}

    app = make_element(doc, apps, 'application', type='normal', **id)

    if desktop:
        make_text(doc, app, 'desktop', desktop)

    position = make_element(doc, app, 'position', force='yes')
    make_text(doc, position, 'x', x)
    make_text(doc, position, 'y', y)

    size = make_element(doc, app, 'size', force='yes')
    make_text(doc, size, 'width', w-6)
    make_text(doc, size, 'height', h-6)


place_app(doc, apps, 'Alacritty', 0, 0, left_width, top_height)
place_app(doc, apps, 'pithos', 0, 0, left_width, top_height)

place_app(doc, apps, 'gvim', 0, y, left_width, bottom_height + 30)

place_app(doc, apps, 'qutebrowser', x, 0, middle_full_width, full_height)
place_app(doc, apps, 'slack', x, 0, middle_full_width, full_height, desktop=8)
place_app(doc, apps, 'Mail', x, 0, middle_full_width, full_height, desktop=8)
place_app(doc, apps, 'outlook.office365.com__mail', x, 0, middle_full_width, full_height, desktop=8)
# Specify the title to avoid affecting "Add Note" windows.
place_app(doc, apps, {'class': 'Zotero', 'title': 'Zotero'}, x, 0, middle_full_width, full_height, desktop=8)

# Generate the applications file.

with open('sections/applications.xml', 'w') as file:
    doc.writexml(file, indent='  ', addindent='  ', newl='\n')
