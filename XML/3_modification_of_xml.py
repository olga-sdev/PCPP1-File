"""
To remove an element of XML file -> remove() method

To add new element to XML -> set() method

To save changes -> tree.write() method
"""

import xml.etree.ElementTree as ET

tree = ET.parse('courses.xml')
root = tree.getroot()

# Example of remove() element
for course in root:
    course.tag = 'course'
    course.remove(course.find('year'))

    for sub_element in course:
        print(course.attrib, sub_element.tag, ':', sub_element.text)

print('===========')

# Example of set() element
for course in root:
    course.tag = 'course'
    if course.get('title') == 'Agile methodolody':
        course.set('time', '4 hours')
    elif course.get('title') == 'Networking':
        course.set('time', '21 hours')
    for sub_element in course:
        print(course.attrib, sub_element.tag, ':', sub_element.text)


tree.write('courses.xml', 'UTF-8', True)


"""
{'title': 'Agile methodolody'} category : Project management
{'title': 'Networking'} category : Information Technology
===========
{'title': 'Agile methodolody', 'time': '4 hours'} category : Project management
{'title': 'Networking', 'time': '21 hours'} category : Information Technology
"""
