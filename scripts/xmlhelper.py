import xml.dom.minidom

# Implements a number of functions that make XML easier to work with.  I don't
# understand why, but the builtin python XML modules are very hard to use on
# their own.

def make_document():
    return xml.dom.minidom.Document()

def make_root(document, tag, **attributes):
    return make_element(document, document, tag, **attributes)

def make_element(document, parent, tag, **attributes):
    element = document.createElement(tag)
    for name, value in attributes.items():
        element.setAttribute(name, value)

    parent.appendChild(element)
    return element

def make_text(document, parent, tag, value):
    element = document.createElement(tag)
    text = document.createTextNode(str(value))

    parent.appendChild(element)
    element.appendChild(text)

    return element

def read_file(file):
    document = xml.dom.minidom.parse(file)
    return document.documentElement

def write_file(document, file):
    document.writexml(file)
