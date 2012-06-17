#!/usr/bin/env python

# This script compiles an OpenBox configuration file by concatenating all the
# XML found in the sections directory.  This allows each section to be in its
# own file, which makes everything more manageable and easier script.

import glob
import xmlhelper

tag = 'openbox_config'
xmlns = 'http://openbox.org/3.4/rc'
output = 'rc.xml'

document = xmlhelper.make_document()
openbox = xmlhelper.make_root(document, tag, xmlns=xmlns)

for path in glob.glob('sections/*.xml'):
    section = xmlhelper.read_file(path)
    openbox.appendChild(section)

with open(output, 'w') as file:
    xmlhelper.write_file(document, file)
