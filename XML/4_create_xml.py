"""
To create element -> apply Element function with two arguments:
* mandatory tag name
* optional attribute dictionary

 dump() method -> for debugging tree/element.

To create sub-elements -> apply SubElement function with three arguments:
* mandatory parent element
* mandatory tag name
* optional attributes of the element

Create a tree object with ElementTree() and save data with write()

New file courses_new.xml is created:
<?xml version='1.0' encoding='UTF-8'?>
<items name="course"><course title="Cognitive Biases" category="Personal development" /></items>
"""

import xml.etree.ElementTree as ET


root = ET.Element('items', {'name': 'course'})
item1 = ET.SubElement(root, 'course', {'title': 'Cognitive Biases', 'category': 'Personal development'})
ET.dump(root)

tree = ET.ElementTree(root)

tree.write('courses_new.xml', 'UTF-8', True)

# <items name="course"><course title="Cognitive Biases" category="Personal development" /></items>
