import xml.etree.ElementTree as ET

# Example with ElementTree and parse method:
print('Example with ElementTree and parse method')
tree = ET.parse('courses.xml')
root = tree.getroot()

for course in root:
    print('\nTag:', course.tag,
          '\nAttribute:', course.attrib)


print('=================')

# Example with fromstring method:
print('Example with fromstring method')
data = """<data>
    <course title="Networking">
        <category>Information Technology</category>
        <year>2024</year>
    </course>
</data>"""

root = ET.fromstring(data)

# Accessing elements
for course in root:
    print('\nTitle of the course:', course.attrib['title'],
          '\nCategory of the course:', course[0].text,
          '\nYear of the course:', course[1].text)

print('=================')


tree = ET.parse('courses.xml')
root = tree.getroot()

# Example: findall method searches the child elements at the first nesting level
for course in root.findall('course'):
    print('Findall method output:', course.get('title'))

# Example: find method returns the first child element containing the specified tag or matching XPath expression
print('Find method output:', root.find('course').get('title'))

# Example: iter method returns all elements
for category in root.iter('category'):
    print('Iter category method output:', category.text)


"""
Example with ElementTree and parse method

Tag: course 
Attribute: {'title': 'Agile methodolody'}
=================
Example with fromstring method

Title of the course: Networking 
Category of the course: Information Technology 
Year of the course: 2024
=================
Findall method output: Agile methodolody
Findall method output: Networking
Find method output: Agile methodolody
Iter category method output: Project management
Iter category method output: Information Technology
"""
